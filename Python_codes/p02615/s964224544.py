from collections import deque
n = int(input())
a_ls = list(map(int, input().split()))
a_ls.sort(reverse = True)
queue = deque()
queue.append(a_ls[0])
for i in range(1,n):
    queue.append(a_ls[i])
    queue.append(a_ls[i])
ans = 0
for _ in range(n-1):
    ans += queue.popleft()
print(ans)


