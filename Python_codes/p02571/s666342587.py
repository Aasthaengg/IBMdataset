s = input()
t = input()
ls = len(s)
lt = len(t)

ans = 0
for i in range(ls-lt+1):
  same = 0
  for j in range(lt):
    ind = i+j
    if s[ind]==t[j]:
      same += 1
  ans = max(ans,same)
print(lt-ans)
