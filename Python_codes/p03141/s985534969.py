N = int(input())
AB = [list(map(int,input().split())) for _ in range(N)]

l = []
T,A = 0,0

for a,b in AB:
  l.append(a+b)
  T += a
  A += b

ans = -A
l.sort(reverse = True)

check = 0

for i in range(N):
  if check == 0:
    ans += l[i]
    check = 1
  else:
    check = 0
print(ans)