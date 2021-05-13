#!/usr/bin/env python
# coding: utf-8

# In[8]:


from bisect import bisect_left,bisect


# In[6]:


N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))


# In[9]:


ans = 0
for b in B:
    i = bisect_left(A,b)
    j = bisect(C,b)
    ans += i*(N-j)
print(ans)


# In[ ]:




