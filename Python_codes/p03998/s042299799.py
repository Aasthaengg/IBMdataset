#!/usr/bin/env python
# coding: utf-8

# In[6]:


from collections import deque


# In[21]:


sa = input()
sb = input()
sc = input()


# In[30]:


def func(s_a, s_b, s_c, n):
    if n == 0:
        if len(s_a) == 0:
            print("A")
            return
        else:
            card = s_a.popleft()
    elif n == 1:
        if len(s_b) == 0:
            print("B")
            return
        else:
            card = s_b.popleft()
    elif n == 2:
        if len(s_c) == 0:
            print("C")
            return
        else:
            card = s_c.popleft()
    
    if card == "a":
        func(s_a,s_b,s_c,0)
    elif card == "b":
        func(s_a,s_b,s_c,1)
    elif card == "c":
        func(s_a,s_b,s_c,2)


# In[31]:


func(deque(sa),deque(sb),deque(sc),0)


# In[ ]:




