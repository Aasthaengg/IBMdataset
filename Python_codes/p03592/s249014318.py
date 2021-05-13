#!/usr/bin/env python
# coding: utf-8

# In[7]:


N,M,K = map(int, input().split())


# In[9]:


for n in range(N+1):
    for m in range(M+1):
        if (N-n)*m + (M-m)*n == K:
            print("Yes")
            break
    else:
        continue
    break
else:
    print("No")


# In[ ]:




