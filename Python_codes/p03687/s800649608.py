from collections import Counter
s = str(input())
l = [chr(i) for i in range(97, 97+26)]

ans = 100
for i in l:
  tmp = s
  cnt = 0
  if i in s:
    while len(Counter(tmp)) > 1:
      c = ''
      for j in range(len(tmp)-1):
        if (tmp[j]==i) or (tmp[j+1]==i):
          c += i
        else:
          c += tmp[j]
      cnt += 1
      tmp = c
    ans = min(ans, cnt)
print(ans)