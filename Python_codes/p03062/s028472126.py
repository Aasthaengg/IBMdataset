#!/usr/bin/env python
# coding: utf-8

# In[8]:


N = int(input())
A = list(map(int, input().split()))


# In[9]:


a_abs = list(map(abs,A))
minus_cnt = sum([1 for x in A if x < 0])
if minus_cnt%2 == 0:
    ans = sum(a_abs)
else:
    ans = sum(a_abs) - min(a_abs)*2
print(ans)


# In[ ]:




