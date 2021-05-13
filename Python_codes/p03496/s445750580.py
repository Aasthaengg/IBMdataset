import sys
import numpy as np
N=int(input())
nums=list(map(int,input().split(" ")))
ans_array=[]
#符号の統一
add=0
mode=0
if min(nums)>0: #全部正の場合
    mode=0
elif max(nums)<0: #全部負の場合
    mode=1
elif max(nums)==min(nums)==0: #全部0
    print("0")
    sys.exit()
else: #正負混合
    mode=2
count=0

if mode==2: #need to modify
    temp=[]
    if abs(max(nums))<abs(min(nums)):
        mode=1 #全部負にする
        add=min(nums)
        ind=np.argmin(nums)
    elif abs(max(nums))>=abs(min(nums)):
        mode=0
        add=max(nums)
        ind=np.argmax(nums)
    for i in range(len(nums)):
        nums[i]+=add
        ans_array.append("{0} {1}".format(ind+1,i+1))
        count+=1
        
        

if mode==0: #全部正
    for i in range(len(nums)-1):
        nums[i+1]+=nums[i]
        count+=1
        ans_array.append("{0} {1}".format(i+1,i+2))
    print(count)
    for i in ans_array:
       print(i)
                

elif mode==1:
    nums.reverse()
    for i in range(len(nums)-1):
        nums[i+1]+=nums[i]
        count+=1    
        ans_array.append("{0} {1}".format(len(nums)-i,len(nums)-i-1))

    print(count)
    for i in ans_array:
       print(i)
