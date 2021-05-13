n = int(input())
min_a = 10**9+1
min_s = 0
max_a = 0
max_s = 0
for i in range(n):
  a,b = map(int, input().split())
  if a<min_a:
    min_a = a
    min_s = b
  if a>max_a:
    max_a = a
    max_s = b

cnt = max_a
cnt += max_s
print(cnt)
