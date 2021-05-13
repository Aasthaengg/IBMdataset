#!/usr/bin/env python
# coding: utf-8

# In[43]:


mylist = list(map(int, input().split()))


# In[45]:


if abs(mylist[0]-mylist[1]) > 10**18:
    print("Unfair")
else:
    if mylist[-1]%2 == 0:
        print(mylist[0]-mylist[1])
    else:
        print(-mylist[0]+mylist[1])


# In[ ]:




