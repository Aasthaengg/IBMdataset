#!/usr/bin/env python
# coding: utf-8

# In[18]:


from collections import deque


# In[12]:


X = input()


# In[26]:


mylist = deque([])
for x in X:
    if x == "S":
        mylist.append("S")
    else:
        if len(mylist) == 0 or mylist[-1] == "T":
            mylist.append("T")
        else:
            mylist.pop()
print(len(mylist))


# In[ ]:




