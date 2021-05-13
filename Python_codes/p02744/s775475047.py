#!/usr/bin/env python
# coding: utf-8

# In[70]:


N = int(input())


# In[71]:


num2alpha = lambda c: chr(c%26+97)


# In[72]:


def dfs(s,n,cnt):
    if n == 0:
        print(s)
        return
    for i in range(cnt+2):
        if i == cnt+1:
            dfs(s+num2alpha(i),n-1,cnt+1)
        else:
            dfs(s+num2alpha(i),n-1,cnt)
dfs("a",N-1,0)


# In[ ]:




