from collections import deque
n = int(input())
q = deque([])
now = 0
reach = [0]*100001
lis = []
for i in range(6):
    lis.append(6**(i+1))
for i in range(5):
    lis.append(9**(i+1))
lis.append(1)
lis = sorted(lis)
q.append(0)
ans = 0
while q:
    if ans == 1:
        break
    x = q.popleft()
    
    for y in lis:
        if x + y < n:
            if  reach[x+y] == 0:
                q.append(x+y)
                reach[x+y] = reach[x]+1
            
        elif x + y == n:
            reach[x+y] = reach[x]+1
            ans = 1
            break
print(max(reach))