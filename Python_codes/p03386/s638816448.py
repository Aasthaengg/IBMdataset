A,B,K=map(int,input().split())
ans=[]
for i in range(A,A+K):
    if A<=i<=B:
        ans.append(i)
    else:
        break
for t in range(B-K+1,B+1):
    if A<=t<=B: 
        ans.append(t)
    else:
        break
for z in sorted(set(ans)):
    print(z)