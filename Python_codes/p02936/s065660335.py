#!/usr/bin/env python
# coding: utf-8

# In[32]:


from collections import deque


# In[37]:


def func():
    N,Q = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int, input().split())
        a,b = a-1,b-1
        graph[a].append(b)
        graph[b].append(a)
    cnt = [0]*N
    for j in range(Q):
        p,x = map(int, input().split())
        cnt[p-1] += x
    q = deque([[0,-1,cnt[0]]])
    d = [-1]*N
    while q:
        cur,fr,p = q.popleft()
        d[cur] = p
        for nex in graph[cur]:
            if nex == fr:
                continue
            q.append([nex,cur,p+cnt[nex]])
    ans = []
    for i in range(N):
        ans.append(d[i])
    print(*ans)


# In[38]:


if __name__ == "__main__":
    func()


# In[ ]:




