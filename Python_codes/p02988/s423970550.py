n=int(input())
P=list(map(int,input().split()))
res=0
for i in range(n-2):
    if P[i]<=P[i+1]<=P[i+2] or P[i]>=P[i+1]>=P[i+2]:
        res+=1
print(res)