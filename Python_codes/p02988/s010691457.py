n = int(input())
p = list(map(int,input().split()))

from collections import deque
temp = deque()
for i in range(3):
    temp.append(p[i])
counter = 0
temp1 = sorted(temp)
if temp[1] == temp1[1]:
    counter += 1
for i in range(n-3):
    temp.popleft()
    temp.append(p[i+3])
    temp1 = sorted(temp)
    if temp[1] == temp1[1]:
        counter += 1
print(counter)