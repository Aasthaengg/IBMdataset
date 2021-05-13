N=int(input())
S=input()
r=S.count('R')
b=S.count('B')
g=S.count('G')
ans=r*b*g
for i in range(N):
    for s in range(N):
        j=i+s
        k=j+s
        if k>=N:
            break
        if S[i]!=S[j] and S[j]!=S[k] and S[k]!=S[i]:
            ans-=1
print(ans)