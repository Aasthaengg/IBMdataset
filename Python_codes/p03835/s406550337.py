#!/usr/bin/env python
# coding: utf-8

# In[4]:


K,S = map(int, input().split())


# In[6]:


ans = 0
for x in range(K+1):
    diff1 = S-x
    if diff1 >= 0:
        for y in range(K+1):
            z = diff1-y
            if z >= 0 and z <= K:
                ans += 1
print(ans)


# In[ ]:




