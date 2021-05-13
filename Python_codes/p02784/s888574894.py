# coding: utf-8
# Your code here!


h,a=map(int,input().split())
A=list(map(int,input().split()))
sum_A=sum(A)
if h>sum_A:
    print("No")

else:
    print("Yes")