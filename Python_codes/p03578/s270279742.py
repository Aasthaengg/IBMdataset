import collections
n = int(input())
d = list(map(str, input().split()))
m = int(input())
t = list(map(str, input().split()))
c_d = collections.Counter(d)
c_t = collections.Counter(t)
ans = ''
for e in c_t:
  if c_t[e] <= c_d[e]:
    next
  else:
    ans = 'NO'
if ans == '':
  ans = 'YES'
print(ans)