#!/usr/bin/env python
# coding: utf-8

# In[7]:


H,W = map(int, input().split())
ans = ["#"*(W+2)]
for _ in range(H):
    ans.append("#"+input()+"#")
ans.append("#"*(W+2))
for col in ans:
    print(col)


# In[ ]:




