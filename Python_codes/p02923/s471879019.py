n = int(input())
h = list(map(int, input().split()))

cnt = [0] * n

for i in range(1, n):
  if h[i - 1] >= h[i]:
    cnt[i] = cnt[i - 1] + 1
  else:
    cnt[i] = 0
        
print(max(cnt))