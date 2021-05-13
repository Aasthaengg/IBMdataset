N = int(input())
AB = [list(map(int,input().split())) for i in range(N)]
AB_sorted = sorted(AB, key=lambda x: x[1])
task_sum = 0
ans = 'Yes'

for i in range(N):
  task_sum += AB_sorted[i][0]
  if task_sum > AB_sorted[i][1]:
    ans = 'No'
    break
print(ans) 