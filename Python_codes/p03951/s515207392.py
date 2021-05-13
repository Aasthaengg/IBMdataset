#!/usr/bin/env python
# coding: utf-8

# In[39]:


N = int(input())
s = str(input())
t = str(input())


# In[40]:


for i in range(len(s)):
#     print(i, s[i:], t[:len(t)-i])
    if s[i:] == t[:len(t)-i]:
#         print(s[:i]+t)
        print(i+N)
        break
    elif i == len(s)-1:
#         print(s+t)
        print(2*N)


# In[ ]:




