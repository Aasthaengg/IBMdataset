import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    K,T=MI()
    a=LI()
    M=max(a)
    if M<=(K+1)//2:
        print(0)
    else:
        temp=sum(a)-M
        ans=M-temp-1
        print(ans)
        

main()
