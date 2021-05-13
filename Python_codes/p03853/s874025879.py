#!/usr/bin/env python
# coding: utf-8

# In[3]:


H,W = map(int, input().split())
C = []
for _ in range(H):
    tmp = input()
    C.append(tmp)
    C.append(tmp)
for i in range(len(C)):
    print(C[i])


# In[ ]:




