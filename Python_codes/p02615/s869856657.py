# coding: utf-8
# Your code here!
N=int(input())

A=list(map(int,input().split()))
A+=A
A.sort(reverse=True)

print(sum(A[1:N]))
