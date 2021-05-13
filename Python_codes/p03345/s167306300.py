# coding: utf-8
# Your code here!
A,B,C,K=map(int,input().split())

all=A+B+C
"""
if K>=2:
    A+=all*4**(K//2-1)
    B+=all*4**(K//2-1)
    C+=all*4**(K//2-1)
"""
if K%2==1:
    A,B,C=B+C,C+A,A+B

ans=A-B
if abs(ans)>10**18:
    print("Unfair")
else:
    print(ans)
