# coding: utf-8
# Your code here!
N=int(input())

print(N-1)
if input()=="Vacant":
    exit()
print(0)
who=input()
if who=="Male":
    start=0
elif who=="Female":
    start=1
else:
    exit()

high=N-1
low=0
while True:
    mid=(high+low)//2
    print(mid)
    who=input()
    if who=="Male":
        temp=0
    elif who=="Female":
        temp=1
    else:
        exit()
    
    if (mid%2)^start==temp:
        low=mid
    else:
        high=mid
    
