s = list(input())
cnt,ans = 0,[]
agct = ["A","G","C","T"]
for i in range(len(s)):
    if s[i] in agct:
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 0
if cnt > 0:
  ans.append(cnt)
print(max(ans))
