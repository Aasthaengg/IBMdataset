#!/usr/bin/env python
# coding: utf-8

# In[16]:


S = int(input())


# In[17]:


x1 = 0; y1 = 0
if S <= 10**9:
    x2 = S; y2 = 0
    x3 = 0; y3 = 1
else:
    x2 = 10**9; y2 = 1
    mod = 10**9
    x3 = (mod - S%mod)%mod
    y3 = (S+x3)//mod
print(x1,y1,x2,y2,x3,y3)


# In[ ]:




