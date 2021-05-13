#!/usr/bin/env python
# coding: utf-8

# In[11]:


N = int(input())
a = list(map(int, input().split()))


# In[12]:


ans = (10**9)*N
x = 0
y = sum(a)
for i in range(N-1):
    x += a[i]
    y -= a[i]
    ans = min(ans,abs(x-y))
    if ans < 2:
        break
print(ans)


# In[ ]:




