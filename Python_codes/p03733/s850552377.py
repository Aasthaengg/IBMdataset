n ,T = map(int, input().split())
t = list(map(int, input().split()))
cnt = T
for i in range(n-1):
  if t[i+1] - t[i] > T:
    cnt += T
  else:
    cnt += t[i+1] - t[i]
print(cnt)