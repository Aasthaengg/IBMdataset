a,b = list(map(int, input().split()))
cnt = 0
while b >= a:
  a = a * 2
  cnt += 1

print(cnt)