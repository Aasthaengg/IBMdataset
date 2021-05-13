#!/usr/bin/env python
# coding: utf-8

# In[5]:


x,y = map(int, input().split())


# In[6]:


if x <= y:
    if abs(x) <= abs(y):
        ans = min(y-x, y-(-x)+1)
    else:
        ans = min(y-x, abs(-y-x)+1)
else:
    ans = abs(abs(x)-abs(y))+1
    if x*y > 0:
        ans += 1
print(ans)


# In[ ]:




