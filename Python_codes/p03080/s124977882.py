

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    s=input()
    r=s.count("R")
    b=N-r
    
    if r>b:
        print("Yes")
    else:
        print("No")

main()
