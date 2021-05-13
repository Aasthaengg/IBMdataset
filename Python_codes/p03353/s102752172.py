import bisect
s = input()
k = int(input())
n = len(s)
ans = []
for i in range(n):
  for j in range(k):
    l = s[i:(i+j+1)]
    if l in ans:
      continue
    bisect.insort_left(ans,l)
  ans = ans[:k]
print(ans[-1])