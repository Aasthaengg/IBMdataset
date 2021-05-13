#!/usr/bin/env python
# coding: utf-8

# In[2]:


N = int(input())


# In[12]:


def lucas(n):
    mylist = [2,1]
    for i in range(2,n+1):
        mylist.append(mylist[i-1]+mylist[i-2])
    return mylist[n]


# In[14]:


print(lucas(N))


# In[ ]:




