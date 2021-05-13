#14:18
n,t = map(int,input().split())
a = list(map(int,input().split()))
b = [0]
for i in range(n)[::-1]:
  b.append(max(b[-1],a[i]))
b.reverse()
b.pop()
#print(b)
c = []
for i in range(n):
  c.append(b[i]-a[i])
c.sort(reverse=True)
#print(c)
cnt = 0
for i in range(n):
  if c[0] == c[i]:
    cnt += 1
  else:
    print(cnt)
    break