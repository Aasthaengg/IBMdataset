#!/usr/bin/env python
# coding: utf-8

# In[15]:


N = int(input())
apb = []
b_sum = 0
for i in range(N):
    A,B = map(int, input().split())
    apb += [A+B]
    b_sum += B


# In[20]:


ans = sum(sorted(apb, reverse=True)[::2])-b_sum
print(ans)


# In[ ]:




