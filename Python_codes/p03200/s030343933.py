S = str(input())
cnt = 0
ans = 0
for i in range(len(S)):
  if S[i] == 'W':
    ans += i
    cnt += 1
ans -= (cnt-1)*cnt//2
print(ans)