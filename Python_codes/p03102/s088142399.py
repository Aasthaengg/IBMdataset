n,m,c = map(int,input().split())
b = [int(x.strip()) for x in input().split()]
a = []
ans = 0
for i in range(n):
  ai = [int(x.strip()) for x in input().split()]
  a.append(ai)
for j in range(n):
  ch = [x*y for (x,y) in zip(a[j],b)]
  ch_sum = sum(ch)
  if ch_sum + c > 0:
    ans += 1
print(ans)