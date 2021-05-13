#!/usr/bin/env python
# coding: utf-8

# In[1]:


S = input()


# In[4]:


f = True
s_reversed = S[::-1]
words = ['maerd', 'remaerd', 'esare', 'resare']
while s_reversed:
    length = len(s_reversed)
    for i in [7,6,5]:
        while s_reversed[:i] in words:
            s_reversed = s_reversed[i:]
    if length == len(s_reversed):
        print("NO")
        f = False
        break
if f:
    print("YES")


# In[ ]:




