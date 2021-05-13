#n=int(input())
n,k=map(int,input().split())
l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
import math
res=math.ceil((n-1)/(k-1))
print(res)