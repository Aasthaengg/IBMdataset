#!/usr/bin/env python
# coding: utf-8

# In[1]:


N = int(input())
A = list(map(int, input().split()))


# In[3]:


ans = 1
p = 0
m = 0
pre = A[0]
for a in A[1:]:
    if a > pre:
        p = 1
    elif a < pre:
        m = 1
    if p == 1 and m == 1:
        ans += 1
        p = 0
        m = 0
    pre = a
print(ans)


# In[ ]:




