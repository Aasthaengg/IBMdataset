a,b,c = map(int, input().split())
k = int(input())

n = max(a,b,c)
ans = sum([a,b,c]) - n
for _ in range(k):
  n *= 2
print(ans+n)