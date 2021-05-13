S=list(input())
min_diff=1000
for i in range(2,len(S)):
  n=int(S[i-2]+S[i-1]+S[i])
  min_diff=min(min_diff,abs(753-n))
print(min_diff)