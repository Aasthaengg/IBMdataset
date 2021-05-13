# coding: utf-8
# Your code here!

def LI():
    return list(map(int,input().split()))
    
n=int(input())
a=LI()
a.sort()
nums=[0]*(10**6+100)
for q in a:
    if nums[q]==0:
        nums[q]=1
        for j in range(2*q,10**6+1,q):
            nums[j]+=9
    elif nums[q]==1:
        nums[q]+=9
        

cnt=0
for i in nums:
    if i==1:
        cnt+=1
print(cnt)