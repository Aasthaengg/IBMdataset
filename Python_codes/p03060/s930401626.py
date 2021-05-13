# coding: utf-8
# Your code here!
N = int(input())
VList = list(map(int, input().split()))
CList = list(map(int, input().split()))
ANS=0
for i in range(N):
    if VList[i]>CList[i]:
        ANS+=VList[i]-CList[i]
print(ANS)