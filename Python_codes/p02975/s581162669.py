# coding: utf-8
# Your code here!
N=int(input())
A=list(map(int,input().split()))
B=list(set(A))

if len(B)==3:
    if B[0]^B[1]==B[2]:
        if A.count(B[0])==A.count(B[1]) and A.count(B[1])==A.count(B[2]):
            print("Yes")
            exit()
elif len(B)==2:
    if 2*A.count(B[0])==A.count(B[1]):
        print("Yes")
        exit()
elif len(B)==1:
    if B[0]==0:
        print("Yes")
        exit()

print("No")