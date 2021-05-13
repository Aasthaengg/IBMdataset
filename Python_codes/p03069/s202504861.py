#!/usr/bin/env python
# coding: utf-8

# In[6]:


N = int(input())
S = input()


# In[9]:


w = S.count(".")
b = 0
ans = min(w,N-w)
for i in range(N):
    if S[i] == ".":
        w -= 1
    else:
        b += 1
    ans = min(ans, w+b)
print(ans)


# In[ ]:




