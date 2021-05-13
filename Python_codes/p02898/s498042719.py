N, K = map(int, input().split())
H = list(map(int, input().split()))
cnt = 0

for i in H:
  if i >= K:
    cnt += 1

print(cnt)