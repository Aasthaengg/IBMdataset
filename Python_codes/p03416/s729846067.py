#!/usr/bin/env python
# coding: utf-8

# In[6]:


A,B = map(int, input().split())


# In[8]:


ans = 0
for x in range(A,B+1):
    x = str(x)
    for i in range(len(x)//2):
        if x[i] != x[-(i+1)]:
            break
    else:
        ans += 1
print(ans)


# In[ ]:




