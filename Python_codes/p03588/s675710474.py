n = int(input())
li = []
for _ in range(n):
  a, b = map(int, input().split())
  li.append((b, a))

li = sorted(li)
ans = li[0][1] + li[0][0]
print(ans)