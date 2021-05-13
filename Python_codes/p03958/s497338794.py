#!/usr/bin/env python
# coding: utf-8

# In[9]:


K,T = map(int, input().split())
a = list(map(int, input().split()))


# In[10]:


if T == 1:
    ans = K-1
else:
    mylist = sorted(a)
    ans = max(mylist[-1]-sum(mylist[:-1])-1,0)
print(ans)

