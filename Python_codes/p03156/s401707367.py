n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))
ans = 0
for i in range(n):
  for j in range(n):
    for k in range(n):
      if 0 < p[i] <= a:
        if a+1 <= p[j] <= b:
          if b+1 <= p[k]:
            ans += 1
            p[i] = 0
            p[j] = 0
            p[k] = 0

print(ans)    