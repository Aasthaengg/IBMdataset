n,k,s=map(int,input().split())
x=[10**9]*n
if s==10**9:x=[1]*n
for i in range(k):x[i]=s
print(*x)