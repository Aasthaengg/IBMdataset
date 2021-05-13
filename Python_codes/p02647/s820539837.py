# coding: utf-8
# Your code here!
N,K=map(int,input().split())

A=list(map(int,input().split()))


for _ in range(K):
    ans=[0]*len(A)
    start=[0]*len(A)
    end=[0]*len(A)
    
    for index,item in enumerate(A):
        start[max(0,index-item)]+=1
        end[min(len(end)-1,index+item)]+=1
    
    #print(start)
    #print(end)
    
    temp=0
    for i in range(len(ans)):
        temp+=start[i]
        ans[i]=temp
        temp-=end[i]
    
    if A==ans:
        break
    else:
        A=ans[:]

print(*ans)