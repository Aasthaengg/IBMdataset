# coding: utf-8
# Your code here!
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
#a=a[::-1]
ans=0
pos=n
pre=0
b=a[0]
for i in range(n):
    x=a.pop()
    if x==0 and pre<=1:
        continue
    elif x>pos-1:
        ans=-1
        break
    else:
        if x==pre-1:
            pre=x
            continue
        else:
            if x>=pre:
                pre=x
                ans+=x
            else:
                ans=-1
                break
    pos-=1
if b>0:
    ans=-1
print(ans)
