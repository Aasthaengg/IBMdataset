import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
E = [[] for i in range(n)]

for i in range(n-1):
  a, b = map(int, input().split())
  E[a-1].append(b-1)
  E[b-1].append(a-1)

c = list(map(int, input().split()))
c.sort()
nums = deque(c)
ans = [0] * n
  
def dfs(cur, pre):
    stack = deque([[cur, pre]])
    while stack:
        cur, pre = stack.pop()
        num = nums.pop()
        ans[cur] = str(num)
        for e in E[cur]:
            if e != pre:
                stack.append([e, cur])

dfs(0, -1)

print(sum(c[:-1]))
print(' '.join(ans))