n=int(input())

S={}
maxr=0
for i in range(n):
    s=input()
    if s in S:
        S[s]+=1
    else:
        S[s]=1

maxc = max(S.values())

ans=[]
for s in S:
    if S[s]==maxc :
        ans.append(s)

ans.sort()
for s in ans:
    print(s)        