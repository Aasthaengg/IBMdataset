N = int(input())
AB = [list(map(int,input().split())) for _ in range(N)]

AB.sort(key=lambda x: x[1])
timer = 0

for i in range(N):
  timer += AB[i][0]
  if timer > AB[i][1]:
    print("No")
    exit()
    
print("Yes")