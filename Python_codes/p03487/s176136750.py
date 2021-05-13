#!/usr/bin/env python
# coding: utf-8

# In[2]:


import collections


# In[15]:


N = int(input())
a = list(map(int, input().split()))


# In[16]:


mycnt = collections.Counter(a)
ans = 0
for x,cnt in mycnt.items():
    if x > cnt:
        ans += cnt
    else:
        ans += cnt - x
print(ans)


# In[ ]:




