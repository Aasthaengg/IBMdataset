N,K=map(int,input().split())
S=input()
ans=""
for x in range(N):
  if x!=K-1:
    ans+=S[x]
  else:
    if S[x]=="A":
      ans+="a"
    elif S[x]=="B":
      ans+="b"
    elif S[x]=="C":
      ans+="c"
print(ans)