N = int(input())
AB = [list(map(int,input().split())) for _ in range(N)]
AB.reverse()
count = 0

for a,b in AB:
  a += count
  if a%b != 0:
    count += (b - (a % b))
  else:
    pass
print(count)