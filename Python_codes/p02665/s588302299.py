n = int(input())
a = list(map(int, input().split()))

if a[0]:
   if n == 0 and a[0] == 1:
      print(1)
   else:
      print(-1)
   exit()

b = [0 for _ in range(n)]
b.append(a[-1])
for i in range(n)[::-1]:
   b[i] = b[i+1] + a[i]

node = 1
ans = 1
for i in range(1, n+1):
   t = min(node*2, b[i])
   ans += t
   node = t - a[i]
   if node < 0:
      print(-1)
      exit()

print(ans)
