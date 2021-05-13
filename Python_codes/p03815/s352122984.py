import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    x=I()
    ans=(x//11)*2
    b=x%11
    if b==0:
        pass
    elif b<=6:
      ans+=1
    else:
        ans+=2
        
    print(ans)  
    

main()
