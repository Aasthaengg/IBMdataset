#!/usr/bin/env python
# coding: utf-8

# In[25]:


N,M = map(int, input().split())
ab = []
mylist = [[] for _ in range(N)]
for _ in range(M):
    ab.append(list(map(int, input().split())))
    mylist[ab[-1][0]-1].append(ab[-1][1])
    mylist[ab[-1][1]-1].append(ab[-1][0])


# In[27]:


ans = [len(cities) for cities in mylist]
for x in ans:
    print(x)


# In[ ]:




