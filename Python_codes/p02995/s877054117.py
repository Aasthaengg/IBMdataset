#!/usr/bin/env python
# coding: utf-8

# In[8]:


import math


# In[5]:


A,B,C,D = map(int, input().split())


# In[14]:


ac = (A-1)//C
bc = B//C
ad = (A-1)//D
bd = B//D
a_both = (A-1)//(C*D//math.gcd(C,D))
b_both = B//(C*D//math.gcd(C,D))
print((B-A+1) - (bc-ac) - (bd-ad) + (b_both-a_both))


# In[ ]:




