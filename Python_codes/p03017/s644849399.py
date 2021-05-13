#!/usr/bin/env python
# coding: utf-8

# In[1]:


N,A,B,C,D = map(int, input().split())
S = input()


# In[3]:


if C < D:
    if S[B-1:D].count("##") == 0 and S[A-1:C].count("##") == 0:
        print("Yes")
    else:
        print("No")
else:
    if S[B-2:D+1].count("...") >= 1 and S[A-1:C].count("##") == 0:
        print("Yes")
    else:
        print("No")


# In[ ]:




