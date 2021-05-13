# 休憩review
# League
from collections import deque
N = int(input())
G = [[] for i in range(N**2+1)]
for i in range(N):
    a = list(map(int, input().split()))
    for j in range(1, N-1):
        _from, _to = a[j-1], a[j]
        G[N*min(i+1, _from)-N+max(i+1, _from)
          ].append(N*min(i+1, _to)-N+max(i+1, _to))


In = [0 for i in range(N**2+1)]  # In[node] = node に入る入次数
for i in range(1, N**2+1):
    for node in G[i]:
        In[node] += 1


stack = deque()
for i in range(1, N**2+1):
    if In[i] == 0:
        stack.append(i)  # stack := 入次数が0になった点を入れておく


Removed = [False for i in range(N**2+1)]  # 考慮されたか
cnt = [1 for i in range(N**2+1)]


while stack:
    x = stack.popleft()
    Removed[x] = True
    for node in G[x]:
        In[node] -= 1
        if In[node] == 0:
            cnt[node] += cnt[x]
            stack.append(node)


all_checked = all(Removed[node] == True for node in range(1, N**2+1))
if all_checked:
    answer = max(cnt)
    print(answer)
    exit()
print(-1)