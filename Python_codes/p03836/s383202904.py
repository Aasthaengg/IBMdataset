#!/usr/bin/env python
# coding: utf-8

# In[20]:


sx,sy,tx,ty = map(int, input().split())


# In[26]:


ans = []
X = sx; Y = sy
for x in range(sx+1,tx+1):
    ans.append("R")
X = x
for y in range(sy+1,ty+1):
    ans.append("U")
Y = y
for x in reversed(range(sx,tx)):
    ans.append("L")
X = x
for y in reversed(range(sy,ty)):
    ans.append("D")
Y = y
Y -= 1
ans.append("D")
for x in range(sx+1,tx+2):
    ans.append("R")
X = x
for y in range(sy,ty+1):
    ans.append("U")
Y = y
X -= 1
ans.append("L")
Y += 1
ans.append("U")
for x in reversed(range(sx-1,tx)):
    ans.append("L")
X = x
for y in reversed(range(sy,ty+1)):
    ans.append("D")
Y = y
X += 1
ans.append("R")
print("".join(ans))


# In[ ]:




