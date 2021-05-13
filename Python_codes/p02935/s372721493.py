import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    v=LI()
    v.sort()
    ans=v[0]
    for i in range(1,N):
        ans=(ans+v[i])/2
    print(ans)

main()
