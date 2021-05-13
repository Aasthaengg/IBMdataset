import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    ans=-1
    
    A,B=MI()
    for i in range(10000):
        a=int(i*0.08)
        b=int(i*0.1)
        
        if a==A and b==B:
            ans=i
            break
        
    print(ans)


main()
