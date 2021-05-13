from collections import deque
K = int(input())
d = deque(["1","2","3","4","5","6","7","8","9"])
ans = 0
for i in range(K):
    now = d.popleft()
    num = int(now[-1])
    if num == 0:
        d.append(now+"0")
        d.append(now+"1")
    elif num == 9:
        d.append(now+"8")
        d.append(now+"9")
    else:
        d.append(now+str(num-1))
        d.append(now+str(num))
        d.append(now+str(num+1))
print(now)