from collections import defaultdict
n=int(input())

d=defaultdict(int)
for i in range(n):
    a,b =map(int,input().split())
    d[b]+=a

d_sorted=sorted(d.items(), key=lambda x: x[0])

time=0
finished=True
for i in range(len(d_sorted)):
    time+=d_sorted[i][1]
    if time>d_sorted[i][0]:
        finished=False
        break

if finished:
    print("Yes")
else:
    print("No")