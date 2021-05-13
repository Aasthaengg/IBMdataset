# coding: utf-8
# Your code here!
n=int(input())
a,b=map(int,input().split())
p=list(map(int,input().split()))
c=0
c1=0
c2=0
for i in range(n):
    if p[i]<=a:
        c+=1
    elif a<p[i]<=b:
        c1+=1
    else:
        c2+=1
print(min(c,c1,c2))