#!/usr/bin/env python
# coding: utf-8

# In[14]:


N = int(input())


# In[15]:


for h in range(1,3500+1):
    for n in range(h,3500+1):
        tmp = 4*h*n - N*n - N*h
        if tmp > 0 and (N*h*n)%tmp == 0:
            w = (N*h*n)//tmp
            print(h,n,w)
            break
    else:
        continue
    break


# In[ ]:




