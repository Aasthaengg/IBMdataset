n = int(input())
tasks = [[0,0] for _ in range(n)]
for i in range(n):
  a, b = map(int, input().split())
  tasks[i][0] = a  # 所要時間
  tasks[i][1] = b  # 締め切り
tasks.sort(key=lambda t: t[1])
t = 0

for i in range(n):
  if t + tasks[i][0] > tasks[i][1]:
    print('No')
    exit()
  t += tasks[i][0]
print('Yes')
