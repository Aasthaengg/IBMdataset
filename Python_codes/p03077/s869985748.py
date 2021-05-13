#!/usr/bin/env python
# coding: utf-8

# In[24]:


N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())


# In[26]:


mylist = [A,B,C,D,E]
x = min(mylist)
ans = -(-N//x)+4
print(ans)


# In[ ]:




