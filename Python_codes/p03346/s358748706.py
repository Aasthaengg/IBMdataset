n = int(input())
c = [int(input()) for i in range(n)]
s = [0]*n
for i,ci in enumerate(c):
  s[ci-1] = i
cnt = 1
ans = n-1
for i in range(n-1):
  if s[i] < s[i+1]:
    cnt += 1
  else:
    ans = min(n-cnt,ans)
    cnt = 1
ans = min(n-cnt,ans)
print(ans)