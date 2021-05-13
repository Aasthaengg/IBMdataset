#!/usr/bin/env python
# coding: utf-8

# In[13]:


N = int(input())
s = []
a = 0
b = 0
ab = 0
cnt = 0
for _ in range(N):
    tmp = input()
    cnt += tmp.count("AB")
    if tmp[0] == "B" and tmp[-1] == "A":
        ab += 1
    elif tmp[0] == "B":
        b += 1
    elif tmp[-1] == "A":
        a += 1
    s.append(tmp)


# In[14]:


if ab==0:
    ans = cnt + min(a,b)
else:
    if a+b>0:
        ans = cnt + ab + min(a,b)
    else:
        ans = cnt + ab-1
print(ans)


# In[ ]:




