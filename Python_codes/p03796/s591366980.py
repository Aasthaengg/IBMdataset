#!/usr/bin/env python
# coding: utf-8

# In[1]:


N = int(input())


# In[2]:


power = 1
for i in range(N):
    power *= (i+1)
    if power > 1000000007:
        power %= 1000000007
print(power)


# In[ ]:




