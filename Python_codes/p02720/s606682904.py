from collections import deque

K = int(input())
d = deque([1,2,3,4,5,6,7,8,9])

for i in range(K-1):
    num = d.popleft()
    mod = num % 10
    if mod != 0:
        d.append(num*10+mod-1)
    d.append(num*10+mod)
    if mod != 9:
        d.append(num*10+mod+1)
print(d.popleft())