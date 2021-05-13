#!/usr/bin/env python
# coding: utf-8

# In[1]:


N = int(input())


# In[14]:


# N = 4
MOD = 10 ** 9 + 7


# In[15]:


char = ['A', 'C', 'G', 'T']
S = [c1 + c2 + c3 for c1 in char for c2 in char for c3 in char]
S


# In[16]:


ng3 = ['AGC', 'GAC', 'ACG']
ng4 = [c + ng for c in char for ng in ng3] + [ng + c for c in char for ng in ng3] + ['A' + c + 'GC' for c in char] + ['AG' + c + 'C' for c in char]
ng4 = set(ng4)
ng4


# In[17]:


dict1 = {s: 1 if s not in ng3 else 0 for s in S}


# In[18]:


for _ in range(N - 3):
    dict2 = {}

    for s in S:
        val = 0
        for c in char:
            if c + s not in ng4:
                val = (val + dict1[c + s[:2]]) % MOD
        dict2[s] = val
    dict1 = dict2


# In[19]:


ans = 0
for s in dict1.keys():
    ans = (ans + dict1[s]) % MOD
print(ans)


# In[ ]:




