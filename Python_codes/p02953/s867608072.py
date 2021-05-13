N=int(input())
arr=list(map(int,input().split()))
ans=1
kari=1
for i in range(N-1):
    kari=max(kari,arr[i]-1)
    
    if kari>arr[i+1]:
        ans=0
        
        break


    
if ans==0:
    print("No")
else:
    print("Yes")
