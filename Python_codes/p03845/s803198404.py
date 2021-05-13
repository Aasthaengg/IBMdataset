n=int(input())
T=list(map(int,input().split()))
m=int(input())
p=[0]*m
x=[0]*m
for i in range(m):
    a,b=map(int,input().split())
    p[i]+=a
    x[i]+=b
tt =sum(T)
for j in range(len(p)):
    ans = tt - T[p[j]-1] + x[j]
    print(ans)