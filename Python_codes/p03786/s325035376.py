#!/usr/bin/env python
# coding: utf-8

# In[26]:


N = int(input())
A = sorted(list(map(int, input().split())))


# In[32]:


tmp = 0
asm = []
for i in range(N):
    tmp += A[i]
    asm += [tmp]
ans = 1
for i in range(2,N+1):
    if asm[-i]*2 >= A[-i+1]:
        ans += 1
    else:
        break
print(ans)


# In[ ]:




