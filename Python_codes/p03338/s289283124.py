n = int(input())
S = input()
ans = 0
for i in range(0,n-1):
  A = set(S[0:i+1])
  B = set(S[i+1:n])
  ans = max(ans,len(list(A&B)))
  
print(ans)