#!/usr/bin/env python
# coding: utf-8

# In[15]:


n = int(input())
a = list(map(int, input().split()))


# In[18]:


a.sort()
ai = max(a)
diff = ai
old = diff
for x in a[:-1]:
    tmp = abs(x-ai/2)
    if tmp <= diff:
        aj = x
        diff = tmp
    if diff == old:
        break
    else:
        old = diff
print(ai,aj)


# In[ ]:




