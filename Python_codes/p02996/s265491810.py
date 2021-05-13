N = int(input())

ab = [list(map(int,input().split())) for _ in range(N)]
AB = sorted(ab, key=lambda x: x[1])

time = 0

for i in range(N):
  time += AB[i][0]
  if time > AB[i][1]:
    print("No")
    exit()
print("Yes")
