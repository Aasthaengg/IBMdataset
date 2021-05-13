import sys
sys.setrecursionlimit(10**9) 
input = sys.stdin.readline
def gdc(a, b):
    if b == 0:
        return a
    return gdc(b, a%b)
def lcm(a,b):
    return a*b//gdc(a,b)

def main():
    N = int(input())
    T = [int(input()) for i in range(N)]
    if N == 1:
        return print(T[0])
    ans = lcm(max(T[0], T[1]), min(T[0], T[1]))
    if N == 2:
        print(ans)
        return
    for i in range(2,N):
        ans = lcm(max(ans, T[i]), min(ans, T[i]))
    print(ans)

if __name__ == '__main__':
    main()