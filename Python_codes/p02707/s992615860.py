N = int(input())
A = map(int, input().split())
cnt = [0]*(N+1)

for i in A:
  cnt[i] += 1

for i in cnt[1:]:
  print(i)