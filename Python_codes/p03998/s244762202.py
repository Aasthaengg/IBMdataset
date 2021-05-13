from collections import deque
s = [deque([ord(a) - ord('a') for a in list(input())]) for i in range(3)]

now = 0
while True:
    if not s[now]:
        print('ABC'[now])
        break
    else:
        now = s[now].popleft()
