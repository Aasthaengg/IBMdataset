import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 18

def main():
    N,x = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    ans = 0
    for a in A:
        if x - a >= 0:
            x -= a
            ans += 1
        else:
            x = 0
            break
    if x > 0:
        ans -= 1
    print(ans)
if __name__ == '__main__':
    main()