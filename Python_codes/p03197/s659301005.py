#!/usr/bin/env python
# coding: utf-8

# In[15]:


N = int(input())
a = []
for _ in range(N):
    a += [int(input())]


# In[16]:


if all([x%2==0 for x in a]):
    print("second")
else:
    print("first")


# In[ ]:




