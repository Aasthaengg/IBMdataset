#!/usr/bin/env python
# coding: utf-8

# In[20]:


S = input()


# In[21]:


mylist = [x for x in S]
if mylist[0] != "A":
    print("WA")
elif mylist[2:-1].count("C") != 1:
    print("WA")
else:
    C_idx = mylist[2:-1].index("C") + 2
    mylist.pop(C_idx)
    if str("".join(mylist[1:])).islower():
        print("AC")
    else:
        print("WA")


# In[ ]:




