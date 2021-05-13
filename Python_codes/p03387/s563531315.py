#!/usr/bin/env python
# coding: utf-8

# In[30]:


abc = list(map(int, input().split()))


# In[32]:


abc_s = sorted(abc)
ones = abc_s[2] - abc_s[1]
twos = -(-(abc_s[2] - (abc_s[0]+ones))//2) + (abc_s[2] - (abc_s[0]+ones))%2
print(ones+twos)


# In[ ]:




