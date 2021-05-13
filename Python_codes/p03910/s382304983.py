#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math


# In[47]:


N = int(input())


# In[48]:


x = int(-(-math.sqrt(N*2)//1))
y = x*(x+1)//2
diff = y - N
while diff > x:
    diff -= x
    x -= 1
for i in range(1,x+1):
    if i != diff:
        print(i)


# In[ ]:




