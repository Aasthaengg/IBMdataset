#!/usr/bin/env python
# coding: utf-8

# In[5]:


W,H,x,y = map(int, input().split())


# In[7]:


s = W*H/2
if x == W/2 and y == H/2:
    p = 1
else:
    p = 0
print(s,p)


# In[ ]:




