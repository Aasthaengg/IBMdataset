import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    A=LI()
    B=LI()
    a=0
    b=0
    for i in range(N):
        if A[i]>B[i]:
            b+=A[i]-B[i]
        elif (B[i]-A[i])%2==0:
            a+=(B[i]-A[i])//2
        else:
            a+=(B[i]+1-A[i])//2
            b+=1
            
    if a>=b:
        print("Yes")
    else:
        print("No")
    

main()
