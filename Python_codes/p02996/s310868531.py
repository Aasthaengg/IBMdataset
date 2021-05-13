n=int(input())
task=[]
for _ in range(n):
  a, b=map(int, input().split())
  task.append([a,b])
task.sort(key=lambda x:x[1])

cula=0
for a, b in task:
  cula+=a
  if cula>b:
    print("No")
    exit()
print("Yes")
