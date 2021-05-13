#!/usr/bin/env python
# coding: utf-8

# In[5]:


H,W,A,B = map(int, input().split())


# In[6]:


for i in range(H):
    if i < B:
        tmp = "0"*A + "1"*(W-A)
    else:
        tmp = "1"*A + "0"*(W-A)
    print(tmp)


# In[ ]:




