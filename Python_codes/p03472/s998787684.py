import heapq
import math
N,H = map(int,input().split())

a_ls = [0]*N
b_ls =[0]*N
for i in range(N):
    a, b = map(int,input().split())
    a_ls[i] = a
    b_ls[i] = -b

a_max = max(a_ls)

heapq.heapify(b_ls)

total = 0
count = 0
for i in range(len(b_ls)):
    b_max = -heapq.heappop(b_ls)

    if a_max>=b_max:
        count += math.ceil((H-total)/a_max)
        total = H
        break
    total += b_max
    count +=1

    if total >=H:
        break

count += math.ceil(max(0,(H-total))/a_max)

print(count)