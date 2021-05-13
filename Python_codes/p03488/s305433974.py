#!/usr/bin/env python
# coding: utf-8

# In[ ]:


s = input()
x, y = map(int, input().split())


# In[17]:


# s = 'FTFFTFFF'


# In[18]:


s = s + 'x'


# In[19]:


s


# In[54]:


renzoku = 1
xyres = [1 << 8000, 1 << 8000]
xy = 0
M = (1 << 16001) - 1
first = s[0] == 'F'
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        renzoku += 1
    else:
#         print(s[i], renzoku)
        if first:
            xyres[0] = 1 << (8000 + renzoku)
            first = False
        else:
            if s[i] == 'F':
                xyres[xy] = (xyres[xy] << renzoku) | (xyres[xy] >> renzoku) & M
            elif renzoku % 2 == 1:
                xy = 1 - xy
        renzoku = 1
        


# In[58]:


if xyres[0] & 1 << (8000 + x) and xyres[1] & 1 << (8000 + y):
    print('Yes')
else:
    print('No')


# In[ ]:




