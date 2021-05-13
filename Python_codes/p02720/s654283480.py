#!/usr/bin/env python
# coding: utf-8

# In[12]:


from collections import deque


# In[1]:


K = int(input())


# In[15]:


q = deque(list(range(1,10)))
for i in range(K-1):
    x = q.popleft()
    if x%10 != 0:
        y = x*10 + x%10 - 1
        q.append(y)
    y = x*10 + x%10
    q.append(y)
    
    if x%10 != 9:
        y = x*10 + x%10 + 1
        q.append(y)
    
ans = q.popleft()
print(ans)


# In[ ]:




