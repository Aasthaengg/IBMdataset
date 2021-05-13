#!/usr/bin/env python
# coding: utf-8

# In[5]:


N = int(input())
K = int(input())
x = list(map(int, input().split()))


# In[7]:


ans = sum([min(p, K-p)*2 for p in x])
print(ans)


# In[ ]:




