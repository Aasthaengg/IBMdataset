#!/usr/bin/env python
# coding: utf-8

# In[20]:


from collections import deque


# In[26]:


s = input()


# In[28]:


S = [x for x in s]
ans = 0
l = 0
r = len(S)-1
while l<r:
    if S[l] == S[r]:
        l += 1
        r -= 1
    else:
        if S[l] == "x":
            l += 1
            ans += 1
        elif S[r] == "x":
            r -= 1
            ans += 1
        else:
            ans = -1
            break
print(ans)


# In[ ]:




