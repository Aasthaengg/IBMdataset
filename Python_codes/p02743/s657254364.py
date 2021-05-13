#!/usr/bin/env python
# coding: utf-8

# In[5]:


a,b,c = map(int, input().split())


# In[7]:


x = c-(a+b)
y = 4*a*b
if x > 0 and x**2 > y:
    print("Yes")
else:
    print("No")


# In[ ]:




