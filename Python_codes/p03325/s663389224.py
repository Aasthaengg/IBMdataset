#!/usr/bin/env python
# coding: utf-8

# In[18]:


N = int(input())
a = list(map(int, input().split()))


# In[19]:


count = [0]*N
for i in range(N):
    while a[i]%2 == 0:
        a[i] = a[i] / 2
        count[i] += 1
print(sum(count))


# In[ ]:




