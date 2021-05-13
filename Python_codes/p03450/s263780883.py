#!/usr/bin/env python
# coding: utf-8

# In[13]:


import sys
from collections import deque
input = sys.stdin.readline


# In[14]:


N, M = map(int, input().split())


# In[2]:


link = [[] for _ in range(N)]
for _ in range(M):
    L, R, D = map(int, input().split())
    link[L-1].append((R-1, D))
    link[R-1].append((L-1, -D))


# In[9]:


def func():
    houmon = [False] * N
    x = [0] * N
    
    for start in range(N):
        if houmon[start]:
            continue
        stack = deque([start])
        while stack:
            n1 = stack.pop()
            houmon[n1] = True
            for n2, d in link[n1]:
                if houmon[n2]:
                    if x[n2] != x[n1] + d:
                        return False
                else:
                    x[n2] = x[n1] + d
                    stack.append(n2)
        
#         if max(x) - min(x) > 10 ** 9:
#             return False
    
    return True


# In[10]:


if func():
    print('Yes')
else:
    print('No')


# In[ ]:




