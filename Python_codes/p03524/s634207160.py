#!/usr/bin/env python
# coding: utf-8

# In[5]:


# import itertools


# In[35]:


S = input()


# In[36]:


# mylist = list(map(lambda x: "".join(x), list(set(itertools.permutations(S)))))
# ngs = []
# for w in ["a","b","c"]:
#     ngs.append(w+w)
#     for x in ["a","b","c"]:
#         ngs.append(w+x+w)
# for word in mylist:
#     for ng in ngs:
#         if ng in word:
#             break
#     else:
#         print("YES")
#         break
# else:
#     print("NO")


# In[39]:


a_cnt = S.count("a")
b_cnt = S.count("b")
c_cnt = S.count("c")
if abs(a_cnt-b_cnt) <= 1 and abs(a_cnt-c_cnt) <= 1 and abs(b_cnt-c_cnt) <= 1:
    print("YES")
else:
    print("NO")


# In[ ]:




