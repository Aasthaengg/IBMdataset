N = int(input())
s = [list(map(int, input().split(" "))) for i in range(N)]

seat = []
for i in range(N):
  a = s[i][1]-s[i][0]+1
  seat.append(a)

print(sum(seat))