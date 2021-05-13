#!/usr/bin/env python
# coding: utf-8

# In[30]:


S = list(input())


# In[31]:


w_count = S.count("W")
print(sum([idx for idx,x in enumerate(S) if x == "W"]) - (w_count-1)*w_count//2)


# In[ ]:




