#!/usr/bin/env python
# coding: utf-8

# In[5]:


K,A,B = map(int, input().split())


# In[6]:


if A >= B-2:
    bisc = K+1
else:
    n = (K-A+1)//2
    bisc = 1+K-2*n+(B-A)*n
print(bisc)


# In[ ]:




