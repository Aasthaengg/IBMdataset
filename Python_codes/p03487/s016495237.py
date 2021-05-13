import collections
N = int(input())
a = list(map(int,input().split()))
ans = 0
c = collections.Counter(a)

key = list(c.keys())


for i in key:
  if i > c[i]:
    ans += c[i]
  elif i < c[i]:
    ans += c[i] - i
print(ans)