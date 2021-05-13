A,B = map(int,input().split())
cnt = 0
for i in range(A,B+1):
  s = str(i)
  ok = 1
  for j in range(len(s)):
    if s[j] != s[len(s)-1-j]:
      ok = 0
  if ok:
    cnt+=1
print(cnt)