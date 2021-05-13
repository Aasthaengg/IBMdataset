

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    a,b,c=input().split()
    if a[-1]==b[0] and b[-1]==c[0]:
        print("YES")
    else:
        print("NO")

main()
