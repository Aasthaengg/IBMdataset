N=int(input())
S=input()
ans=0
for i in range(N):
  ans=max(ans,len(list(set(list(set(list(S[:i+1])) & set(list(S[i+1:])))))))
print(ans)