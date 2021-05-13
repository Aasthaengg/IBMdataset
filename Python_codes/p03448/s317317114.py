#!/usr/bin/env python
# coding: utf-8

# In[20]:


A = int(input())
B = int(input())
C = int(input())
X = int(input())


# In[22]:


ans = 0
for a in range(min(X//500+1, A+1)):
    for b in range(min((X-500*a)//100+1, B+1)):
        c = (X-500*a-100*b)//50
#         print(a,b,c)
        if c <= C:
            ans += 1
print(ans)


# In[ ]:




