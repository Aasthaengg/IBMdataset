N=int(input())
A=list(map(int,input().split()))
A=sorted(A)
nums=[]
num=0
ans=1
for a in A:
    num+=a
    nums.append(num)
for n in range(N-2,-1,-1):
    if nums[n]*2>=A[n+1]:
        ans+=1
    else:
        break
print(ans)
