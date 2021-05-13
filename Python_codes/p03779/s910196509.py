#!/usr/bin/env python
# coding: utf-8

# In[5]:


X = int(input())


# In[6]:


p = 0
for i in range(1,X+1):
    p += i
    if p >= X:
        print(i)
        break


# In[ ]:




