#!/usr/bin/env python
# coding: utf-8

# In[27]:


x1,y1,x2,y2 = map(int, input().split())


# In[28]:


import numpy as np


# In[29]:


rot = np.array([[0, -1], [1, 0]])
vec0 = np.array([x1, y1])
vec1 = np.array([x2-x1, y2-y1])
vec2 = np.dot(rot, vec1)
vec3 = np.dot(rot, vec2)
ans = list(map(str, list(vec0 + vec1 + vec2) + list(vec0 + vec1 + vec2 + vec3)))
print(" ".join(ans))


# In[ ]:




