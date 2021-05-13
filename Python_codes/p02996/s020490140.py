N=int(input())
task=[tuple(map(int,input().split())) for _ in [0]*N]
task.sort(key=lambda x:x[1])
time=0
flg=True
for a,b in task:
    time+=a
    if b<time:
        flg=False
print(['No','Yes'][flg])