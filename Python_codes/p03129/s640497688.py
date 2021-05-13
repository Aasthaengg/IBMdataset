#coding:utf-8

I=raw_input()
n,k=map(int, I.split(" "))

def f(n):
    if n<3:return 0
    if n==3:return 2
    if n%2==0:return f(n-1)
    return f(n-1)+1

if f(n)>=k or k==1:
    print("YES")
else:
    print("NO")