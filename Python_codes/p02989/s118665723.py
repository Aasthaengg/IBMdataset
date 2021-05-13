import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    d=LI()
    d.sort()
    a=d[N//2-1]
    b=d[N//2]
    ans=b-a
    print(ans)

main()
