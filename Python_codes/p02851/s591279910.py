from itertools import accumulate
n,k=map(int, input().split()) 
A=list(map(int, input().split()))
S=[0]+list(accumulate(A))
R=[(S[i]-i)%k for i in range(n+1)]

r_dict={}
ans=0
for i in range(n+1):
    if R[i] in r_dict:
        ans+=r_dict[R[i]]
        r_dict[R[i]]+=1
    else:
        r_dict[R[i]]=1
    if i-k+1>=0:
        r_dict[R[i-k+1]]-=1
    
print(ans)