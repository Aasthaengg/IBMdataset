#!/usr/bin/env python
# coding: utf-8

# In[17]:


n = int(input())
a = list(map(int, input().split()))


# In[19]:


if n%2 == 0:
    ans = list(reversed([a[i] for i in range(n) if i%2 != 0]))
    ans += [a[i] for i in range(n) if i%2 == 0]
else:
    ans = list(reversed([a[i] for i in range(n) if i%2 == 0]))
    ans += [a[i] for i in range(n) if i%2 != 0]
print(*ans)


# In[ ]:




