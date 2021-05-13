#!/usr/bin/env python
# coding: utf-8

# In[19]:


N = int(input())


# In[20]:


k = len(str(N))
if N%(10**(k-1)) == 10**(k-1) - 1:
    print(int(N/(10**(k-1))) + 9*(k-1))
else:
    print(int(N/(10**(k-1))) + 9*(k-1) - 1)


# In[ ]:




