import sys

def main(apples,ln):
    minp=apples[0]
    profit=[0,0]
    for x in range(1,n):
        minp=min(apples[x],minp)
        if profit[1]<apples[x]-minp:
            profit[0]=1
            profit[1]=apples[x]-minp
        elif profit[1]==apples[x]-minp:
            profit[0]+=1
    return profit[0]

n,t=map(int, sys.stdin.readline().strip().split())
apples=list(map(int,sys.stdin.readline().strip().split()))

print(main(apples,n))
