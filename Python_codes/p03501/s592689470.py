
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
mod=10**9+7

def main():
    n,a,b=MI()
    print(min(n*a,b))


main()