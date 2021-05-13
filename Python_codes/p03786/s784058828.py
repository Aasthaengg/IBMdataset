n=int(input())
A=list(map(int,input().split()))
A.sort()
S=[]
s=0
for i in range(n):
    s+=A[i]
    S.append(s)
ans=1
for i in reversed(range(n-1)):
    if S[i]*2>=A[i+1]:
        ans+=1
    else:
        break
print(ans)