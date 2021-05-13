from collections import deque
n = int(input())
L = list(range(1, 10))
count = 9
d = deque([1,2,3,4,5,6,7,8,9])
while count < n:
    p = d.popleft()
    p1 = p%10
    if p1 == 0:
        lunlun = p*10 + p1
        d.append(lunlun)
        L.append(lunlun)
        count += 1
        lunlun += 1
        d.append(lunlun)
        L.append(lunlun)
        count += 1
    elif p1 == 9:
        lunlun = p*10 + p1 - 1
        d.append(lunlun)
        L.append(lunlun)
        count += 1
        lunlun += 1
        d.append(lunlun)
        L.append(lunlun)
        count += 1
    else:
        lunlun = p*10 + p1 - 1
        d.append(lunlun)
        L.append(lunlun)
        count += 1
        lunlun += 1
        d.append(lunlun)
        L.append(lunlun)
        count += 1
        lunlun += 1
        d.append(lunlun)
        L.append(lunlun)
        count += 1
print(L[n-1])
