#!/usr/bin/env python
# coding: utf-8

# In[11]:


N = int(input())
A = list(map(int, input().split()))


# In[12]:


even_list = [x for x in A if x%2 == 0]
ans = 3**len(A) - 2**(len(even_list))
print(ans)


# In[ ]:




