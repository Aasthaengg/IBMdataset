#!/usr/bin/env python
# coding: utf-8

# In[6]:


import math


# In[7]:


def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


# In[15]:


N,P = map(int, input().split())
A = list(map(int, input().split()))


# In[16]:


even_cnt = sum([1 for x in A if x%2 == 0])
odd_cnt = sum([1 for x in A if x%2 != 0])
if P == 0:
    ans1 = 2**even_cnt
    ans2 = 0
    for i in range(0,odd_cnt+1,2):
        ans2 += comb(odd_cnt,i)
else:
    ans1 = 2**even_cnt
    ans2 = 0
    for i in range(1,odd_cnt+1,2):
        ans2 += comb(odd_cnt,i)
print(ans1*ans2)


# In[ ]:




