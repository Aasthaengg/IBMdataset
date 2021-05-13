m = int(input())
s = input().rstrip()
def zalgo(s):
  n = len(s)
  lcp = [0]*n
  lcp[0] = n
  i = 1
  j = 0
  while i < n:
    while i+j < n and s[j] == s[i+j]:
      j += 1
    lcp[i] = j
    if j == 0:
      i += 1
      continue
    k = 1
    while i+k < n and k+lcp[k] < j:
      lcp[i+k] = lcp[k]
      k += 1
    i += k
    j -= k
  return lcp
ans = 0
for i in range(m):
  ss = s[i:]
  lcp = zalgo(ss)
  ans = max([ans]+[min(lcp[j],j) for j in range(m-i)])
print(ans)