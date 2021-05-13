import sys
def input():
    return sys.stdin.readline()[:-1]
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = A[0]
    for e in A[1:]:
        ans = gcd(ans,e)
    print(ans)
if __name__ == '__main__':
    main()
