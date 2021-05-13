#!/usr/bin/env python
# coding: utf-8

# In[12]:


import collections


# In[10]:


N = int(input())
s = []
for _ in range(N):
    s.append(input())


# In[30]:


ans = 0
mydict = {}
for i in range(N):
    tmp = "".join(sorted(s[i]))
    if tmp not in mydict:
        mydict[tmp] = 1
    else:
        ans += mydict[tmp]
        mydict[tmp] += 1
print(ans)

