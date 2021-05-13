N, T = map(int,input().split())
AN = list(map(int,input().split()))

maximum = 0
ans = 0
left = AN[0]

for n in range(1,N):
  if AN[n]-left == maximum:
    ans += 1
  elif AN[n]-left > maximum:
    maximum = AN[n]-left
    ans = 1

  left = min(left,AN[n])

print(ans)