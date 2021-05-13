from collections import Counter

S=input()
T=input()
A=dict(Counter(list(S)))
B=dict(Counter(list(T)))

ans="Yes"
for m in A:
  for n in B:
    if A[m]==B[n]:
      del B[n]
      break
  else:
    ans="No"
    break
print(ans)