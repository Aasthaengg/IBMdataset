n=int(input())
a=list(map(int,input().split()))
b=dict()
for x in a:
  if x in b:
    b[x] += 1
  else:
    b[x] = 1
ans = 0
for k, v in b.items():
  if k < v:
    ans += v - k
  elif k > v:
    ans += v
print(ans)