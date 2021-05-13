#!/usr/bin/env python
# coding: utf-8

# In[27]:


L,R = map(int, input().split())


# In[30]:


MOD = 2019
res = MOD
if R - L < MOD:
    for l in range(L, R):
        for r in range(l+1, R+1):
            res = min(res, (l * r) % MOD)
else:
    res = 0
print(res)

