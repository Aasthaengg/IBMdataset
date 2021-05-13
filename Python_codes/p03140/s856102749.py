N = int(input())
S1 = input()
S2 = input()
S3 = input()
ans = 0
for i in range(N):
  if S1[i] == S2[i] == S3[i]:
    ans += 0
  elif S1[i] != S2[i] and S2[i] != S3[i] and S3[i] != S1[i]:
    ans += 2
  else:
    ans += 1
print(ans)