#!/usr/bin/env python
# coding: utf-8

# In[12]:


abc = list(map(int, input().split()))


# In[13]:


if abc[0]%2 == 0 or abc[1]%2 == 0 or abc[2]%2 == 0:
    print(0)
else:
    abc_s = sorted(abc)
    print(abc_s[0]*abc_s[1])


# In[ ]:




