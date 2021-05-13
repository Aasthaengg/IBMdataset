#!/usr/bin/env python
# coding: utf-8

# In[8]:


N = int(input())
S = input()


# In[19]:


ans = 0
for i in range(10):
    str_i = str(i)
    i_index = S.find(str_i)
    if i_index == -1:
        continue
    for j in range(10):
        str_j = str(j)
        j_index = S.find(str_j, i_index+1)
        if j_index == -1:
            continue
        for k in range(10):
            str_k = str(k)
            k_index = S.find(str_k, j_index+1) 
            if k_index != -1:
                ans += 1
print(ans)


# In[ ]:




