n=int(input())
a,b=map(int,input().split())
l=list(map(int,input().split()))

c0=0
c1=0
c2=0
for i in range(n):
    if l[i]<=a:
        c0+=1
    if a<l[i]<=b:
        c1+=1
    if l[i]>b:
        c2+=1
print(min(c0,c1,c2))