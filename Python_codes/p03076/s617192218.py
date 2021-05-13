#!/usr/bin/env python
# coding: utf-8

# In[17]:


abcde = []
for _ in range(5):
    abcde.append(int(input()))
print(sum(-(-x//10)*10 for x in abcde) + min(x%10 if x%10 != 0 else 10 for x in abcde ) - 10)


# In[ ]:




