#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math


# In[25]:


N,M = map(int, input().split())
S = input()
T = input()


# In[26]:


g = math.gcd(N,M)
for i in range(g):
    if S[(N//g)*i] != T[(M//g)*i]:
        print(-1)
        break
else:
    print(N*M//g)


# In[ ]:




