from collections import deque
n = int(input())
b = list(map(int,input().split()))
ans = deque()
for _ in range(n):
    for i in range(len(b))[::-1]:
        if b[i] == i + 1:
            ans.appendleft(b[i])
            b.pop(i)
            break
        if i == 0:
            print(-1)
            exit(0)
for i in ans:
    print(i)