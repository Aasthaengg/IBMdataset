n=int(input())
a=[]
for _ in range(n):
    i,j=map(int,input().split())
    a+=[[i+j,i-j]]
a.sort()
b,c=-10**9,0
for i,j in a:
    if j>=b:
        c+=1
        b=i
print(c)