#!/usr/bin/env python
# coding: utf-8

# In[19]:


N,K = map(int, input().split())
mydict = {}
for _ in range(N):
    a,b = map(int, input().split())
    if a not in mydict:
        mydict[a] = b
    else:
        mydict[a] += b


# In[20]:


mydict_s = sorted(mydict.items(), key=lambda x:x[0])
cnt = 0
for i,items in enumerate(mydict_s):
    cnt += items[1]
    if cnt >= K:
        ans = items[0]
        break
print(ans)


# In[ ]:




