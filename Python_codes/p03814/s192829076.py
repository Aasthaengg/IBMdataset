#!/usr/bin/env python
# coding: utf-8

# In[10]:


s = input()
print(len(s) - list(reversed(s)).index("Z") - s.index("A"))


# In[ ]:




