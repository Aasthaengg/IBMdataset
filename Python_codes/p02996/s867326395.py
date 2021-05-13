N = int(input())
job = []
for _ in range(N):
    a,b = map(int,input().split())
    job.append((a,b))
from operator import itemgetter
job_sort = sorted(job, key = itemgetter(1))
import sys
time = 0
for i in range(N):
    time += job_sort[i][0]
    if time>job_sort[i][1]:
        print("No")
        sys.exit()
print("Yes")