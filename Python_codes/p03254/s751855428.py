#!/usr/bin/env python
# coding: utf-8

# In[17]:


N,x = map(int, input().split())
a = list(map(int, input().split()))


# In[18]:


a_sum = sum(a)
if a_sum == x:
    print(N)
elif a_sum < x:
    print(N-1)
else:
    for i in range(N):
        if x < sum(sorted(a, reverse=False)[:i+1]):
            print(i)
            break


# In[ ]:




