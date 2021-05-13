#!/usr/bin/env python
# coding: utf-8

# In[24]:


N, T = map(int, input().split())
t = list(map(int, input().split()))


# In[25]:


ans = 0
mylist = [t[i+1] - t[i] for i in range(len(t)-1)]
for x in mylist:
    if x > T:
        ans += T
    else:
        ans += x
print(ans+T)


# In[ ]:




