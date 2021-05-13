from sys import stdin
import string
import heapq
h,w = map(int,stdin.readline().rstrip().split())
s = ""
for i in range(h):
    s += stdin.readline().rstrip()
task_4 = (h//2)*(w//2)
task_2 = (h%2)*(w//2)+(w%2)*(h//2)
task_1 = (h%2)*(w%2)
alpha = string.ascii_lowercase
li = [-s.count(i) for i in alpha if s.count(i) != 0]
heapq.heapify(li)
for i in range(task_4):
    if li[0] <= -4:
        k = heapq.heappop(li)
        if k+4 == 0:
            continue
        else:
            heapq.heappush(li,k+4)
    else:
        print("No")
        exit()
for i in range(task_2):
    if li[0] <= -2:
        k = heapq.heappop(li)
        if k+2 == 0:
            continue
        else:
            heapq.heappush(li,k+2)
    else:
        print("No")
        exit()
for i in range(task_1):
    if li[0] <= -1:
        k = heapq.heappop(li)
        if k+1 == 0:
            continue
        else:
            heapq.heappush(li,k+1)
    else:
        print("No")
        exit()
print("Yes")