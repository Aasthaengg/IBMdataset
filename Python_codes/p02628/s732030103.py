n, k = map(int, input().split())
p = input().split()
p_n = sorted(p, key=int)
ans = 0
for i in range(k):
  ans += int(p_n[i])
print(ans)