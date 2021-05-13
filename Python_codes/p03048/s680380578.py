#!/usr/bin/env python
# coding: utf-8

# In[1]:


rgbn = list(map(int, input().split()))


# In[2]:


mylist = sorted(rgbn[:3], reverse=True)
ans = 0
for i in range(rgbn[3]//mylist[0] + 1):
#     print(i)
    for j in range((rgbn[3] - mylist[0]*i)//mylist[1] + 1):
#         print(i,j)
        rest = (rgbn[3] - mylist[0]*i - mylist[1]*j)
        if rest%mylist[2] == 0:
#             print(i,j,rest//mylist[2])
            ans += 1
print(ans)


# In[ ]:




