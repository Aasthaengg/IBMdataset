#!/usr/bin/env python
# coding: utf-8

# In[13]:


D,N = map(int, input().split())


# In[15]:


if N != 100:
    print(N*(100**D))
elif N == 100:
    print((N+1)*100**D)


# In[ ]:




