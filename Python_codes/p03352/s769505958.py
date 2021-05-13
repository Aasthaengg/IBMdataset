#!/usr/bin/env python
# coding: utf-8

# In[20]:


X = int(input())


# In[22]:


for i in range(X+1)[::-1]:
    for j in range(2,i):
        p = 2
        flag = False
        while flag == False:
            if j**p == i:
                print(i)
                flag = True
                break
            elif j**p > i:
                break
            else:
                p += 1
        if flag:
            break
    else:
        continue
    break
else:
    print(1)


# In[ ]:




