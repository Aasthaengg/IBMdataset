import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N = int(input())

chars = "abcdefghij"

queue = deque()
queue.append(('a', 1))

ans = []

while queue:
    s, num = queue.popleft()
    if len(s) == N:
        print(s)
    else:
        for i in range(num+1):
            ss = s + chars[i]
            if i == num:
                queue.append((ss, num+1))
            else:
                queue.append((ss, num)) 