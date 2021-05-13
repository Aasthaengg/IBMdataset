#!/usr/bin/env python
# coding: utf-8

# In[11]:


import itertools


# In[20]:


N = int(input())
S = {}
S["M"] = 0
S["A"] = 0
S["R"] = 0
S["C"] = 0
S["H"] = 0
for _ in range(N):
    tmp = input()
    if tmp[0] == "M":
        S["M"] += 1
    elif tmp[0] == "A":
        S["A"] += 1
    elif tmp[0] == "R":
        S["R"] += 1
    elif tmp[0] == "C":
        S["C"] += 1
    elif tmp[0] == "H":
        S["H"] += 1


# In[21]:


ans = 0
for myset in list(itertools.combinations("MARCH",3)):
    ans += S[myset[0]]*S[myset[1]]*S[myset[2]]
print(ans)


# In[ ]:




