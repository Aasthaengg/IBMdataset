

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    s=input()
    if len(s)==2:
        print(s)
    else:
        print(s[::-1])

main()
