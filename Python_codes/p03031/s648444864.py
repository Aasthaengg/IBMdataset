#!/usr/bin/env python
# coding: utf-8

# In[15]:


N,M = map(int, input().split())
ks = []
for _ in range(M):
    ks.append(list(map(int, input().split())))
p = list(map(int, input().split()))


# In[16]:


ans = 0
for s in range(2**N):
    s_bit = format(s,"010b")
    for i,item in enumerate(ks):
        cnt = 0
        for x in item[1:]:
            if s_bit[10-x] == "1":
                cnt += 1
        if cnt%2 != p[i]:
            break
    else:
        ans += 1
        continue
print(ans)


# In[ ]:




