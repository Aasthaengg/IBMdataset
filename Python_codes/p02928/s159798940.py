#!/usr/bin/env python
# coding: utf-8

# In[42]:


N,K = map(int, input().split())
A = list(map(int, input().split()))


# In[44]:


ans1 = 0
ans2 = 0
for i,a in enumerate(A):
    for j,a_ in enumerate(A):
        if i > j:
            if a > a_:
                ans2 += 1
        if i < j:
            if a > a_:
                ans1 += 1
                ans2 += 1
print((ans1*K + ans2*(K*(K-1)//2))%(10**9+7))


# In[ ]:




