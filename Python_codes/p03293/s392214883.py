#!/usr/bin/env python
# coding: utf-8

# In[1]:


S = input()
T = input()


# In[4]:


for i in range(len(S)):
    tmp = S[i:] + S[:i]
    if tmp == T:
        print("Yes")
        break
else:
    print("No")


# In[ ]:




