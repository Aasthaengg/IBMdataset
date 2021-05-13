S = str(input())

ans = 0
cnt = 0
for i in range(len(S)):
  if (S[i]=='A') or (S[i]=='T') or (S[i]=='C') or (S[i]=='G'):
    cnt += 1
  else:
    ans = max(ans, cnt)
    cnt = 0
ans = max(ans, cnt)
print(ans)