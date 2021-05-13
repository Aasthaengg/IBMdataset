#!/usr/bin/env python
# coding: utf-8

# In[16]:


N = int(input())
AB = []
for _ in range(N):
    AB.append(list(map(int, input().split())))


# In[17]:


x = 0
ans = 0
for i in reversed(range(N)):
    A,B = AB[i]
    b = -(-AB[i][0]//AB[i][1])*AB[i][1]
    if b-A >= x:
        ans += b-A-x
        x = b-A
    else:
        b = -(-(AB[i][0]+x)//AB[i][1])*AB[i][1]
        ans += b-A-x
        x = b-A
print(ans)


# In[ ]:




