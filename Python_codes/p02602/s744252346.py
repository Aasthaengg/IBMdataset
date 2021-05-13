import sys
input = sys.stdin.readline

n,k=map(int,input().split())
L=list(map(int,input().split()))

ans=[]
for i in range(k,n):
    if L[i]>L[i-k]:
        print('Yes')
    else:
        print('No')
            
