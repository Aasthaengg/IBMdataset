#!/usr/bin/env python
# coding: utf-8

# In[11]:


N,C,K = map(int, input().split())
T = []
for i in range(N):
    T.append(int(input()))


# In[13]:


T = sorted(T)
ans = 0
p = 0
t = 0
for i in range(N):
    if t == 0:
        t = T[i]
    if T[i] <= t+K:
        p += 1
        if p >= C:
            ans += 1
            p = 0
            t = 0
    else:
        t = T[i]
        ans += 1
        p = 1
if p > 0:
    ans += 1
print(ans)


# In[ ]:




