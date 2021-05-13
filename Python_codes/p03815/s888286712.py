# coding: utf-8
# Your code here!
n=int(input())
cnt=n//11
cnt*=2
if 0<n%11<=6:
    cnt+=1
elif n%11>6:
    cnt+=2
print(cnt)
