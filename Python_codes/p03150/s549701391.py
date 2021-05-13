#!/usr/bin/env python
# coding: utf-8

# In[22]:


S = input()


# In[24]:


keyence = "keyence"
length = len(keyence)
flag = True
for i in range(len(keyence)):
#     print(S[:i+1], keyence[:i+1], S[-length+i+1:], keyence[-length+i+1:])
    if S[:i+1] == keyence[:i+1]:
        if S[-length+i+1:] == keyence[-length+i+1:]:
            print("YES")
            flag = False
            break
if flag:
    print("NO")


# In[ ]:




