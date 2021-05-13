n = int(input())
d, x = map(int, input().split())
dic = {}
for i in range(n):
  a = int(input())
  dic[i] = [a *(j - 1) + 1 for j in range(2, d + 1) if a *(j - 1) + 1 <= d]
ans = 0
for v in dic.values():
  ans += len(v)
ans += n + x
print(ans)