#!/usr/bin/env python
# coding: utf-8

# In[8]:


N = int(input())
D,X = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))


# In[9]:


ans = 0
for i in range(N):
    ans += -(-D//A[i])
ans += X
print(ans)


# In[ ]:




