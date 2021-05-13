n = int(input())
Al = list(map(int, input().split()))
cnt= 1

for a in Al:
  if a == cnt:
    cnt += 1
print(-1 if cnt == 1 else n - (cnt-1))