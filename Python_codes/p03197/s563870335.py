# coding: utf-8
# Your code here!
N=int(input())

A=[]
for _ in range(N):
    A.append(int(input()))
    
B=list(map(lambda x : x%2,A))

if B.count(0)==len(B):
    print("second")
else:
    print("first")