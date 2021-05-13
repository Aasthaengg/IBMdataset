n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

ans = 0
min_d = 10 ** 7
for i in range(n):
  tp = t - h[i] * 0.006
  ab = abs(a - tp)
  min_d = min(min_d, ab)
  
  if min_d == ab:
    ans = i+1
print(ans)