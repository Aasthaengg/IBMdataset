# coding: utf-8
# Your code here!

def fibo(n):
    if n==0:
        return 1
    if n==1:
        return 1
    if memo[n] != 0:
        return memo[n]
    memo[n]=fibo(n-1)+fibo(n-2)
    return memo[n]
n=int(input())
memo=[0 for i in range(n+1)]

print(fibo(n))
