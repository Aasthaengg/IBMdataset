# coding: utf-8
# Your code here!
# coding: utf-8
# Your code here!
N=int(input())
A=list(map(int,input().split()))

for i in range(N):
    A[i]-=(i+1)

A.sort()

temp1=A[N//2]
temp2=A[N//2-1]

ans1=0
for i in range(N):
    ans1+=abs((A[i])-temp1)

ans2=0
for i in range(N):
    ans2+=abs((A[i])-temp2)
    
print(min(ans1,ans2))