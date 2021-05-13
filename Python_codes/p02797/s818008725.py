#!/usr/bin/env python
# coding: utf-8

# In[1]:


N,K,S = map(int, input().split())


# In[4]:


if S < 10**9:
    ans = [S]*K + [S+1]*(N-K)
elif S == 10**9:
    ans = [S]*K + [1]*(N-K)
print(*ans)


# In[ ]:




