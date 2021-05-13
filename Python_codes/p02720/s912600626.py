from collections import deque

K = int(input())
L = deque()
for i in range(9):
    L.append((i+1))

for i in range(K):
    ans = L.popleft()
    if ans % 10:
        L.append(10*ans+ans%10-1)
    L.append(10*ans+ans%10)
    if ans % 10-9:
        L.append(10*ans+ans%10+1)

print(ans)