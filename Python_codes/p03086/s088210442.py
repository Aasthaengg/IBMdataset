S = list(input())
ans = 0
n_ans = 0
for i in range(len(S)):
  if(S[i]=='A' or S[i]=='C' or S[i]=='G' or S[i]=='T'):
    n_ans += 1
  else:
    ans = max(ans, n_ans)
    n_ans = 0
ans = max(ans, n_ans)
print(ans)