#!/usr/bin/env python
# coding: utf-8

# In[25]:


N = int(input())
X = list(map(int, input().split()))


# In[26]:


x1 = sorted(X)[N//2-1]
x2 = sorted(X)[N//2]
for i in range(N):
    if X[i] >= x2:
        print(x1)
    else:
        print(x2)


# In[ ]:




