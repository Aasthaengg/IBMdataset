#!/usr/bin/env python
# coding: utf-8

# In[22]:


N,M = map(int, input().split())
ab = []
for _ in range(M):
    ab.append(list(map(int, input().split())))


# In[23]:


start = [sorted(ship)[1] for ship in ab if 1 in ship]
goal = [sorted(ship)[0] for ship in ab if N in ship]
if set(start) & set(goal):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")


# In[ ]:




