#!/usr/bin/env python
# coding: utf-8

# In[7]:


N = int(input())
A = []
for _ in range(2):
    A.append(list(map(int, input().split())))


# In[8]:


ans = 0
for i in range(N):
    ans = max(ans, sum(A[0][:i+1])+sum(A[1][i:]))
print(ans)


# In[ ]:




