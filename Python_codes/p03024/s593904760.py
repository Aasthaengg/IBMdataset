

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    S=input()
    N=len(S)
    ans=15-N+S.count("o")
    if ans>=8:
        print("YES")
    else:
        print("NO")

main()
