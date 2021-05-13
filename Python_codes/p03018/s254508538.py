#!/usr/bin/env python
# coding: utf-8

# In[1]:


s = input()


# In[6]:


s_ = s.replace("BC","D")
cnt = 0
ans = 0
for i in range(len(s_)):
    if s_[i] == "A":
        cnt += 1
    elif s_[i] == "D":
        ans += cnt
    else:
        cnt = 0
print(ans)


# In[ ]:




