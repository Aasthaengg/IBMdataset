#!/usr/bin/env python
# coding: utf-8

# In[9]:


N = int(input())
X = []; Y = []
for _ in range(N):
    x,y = map(int, input().split())
    X += [x]
    Y += [y]


# In[10]:


dic = {}
for i in range(N):
    for j in range(N):
        if i != j:
            x = X[i]-X[j]
            y = Y[i]-Y[j]
            dic[(x,y)] = dic.get((x,y),0) + 1
if N == 1:
    print(1)
else:
    print(N-max(dic.values()))


# In[ ]:




