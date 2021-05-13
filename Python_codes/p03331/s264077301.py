N = int(input())
ans = 100
i = 1
while i * 2 <= N:
  ans = min(ans, sum(map(int, list(str(i)))) + sum(map(int, list(str(N-i)))))
  i += 1
print(ans)