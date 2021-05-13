#!/usr/bin/env python
# coding: utf-8

# In[15]:


from collections import deque


# In[38]:


N,M = map(int, input().split())
alist = [False]*N
for _ in range(M):
    alist[int(input())-1] = True


# In[41]:


dp = deque([0]*2)
dp[0] = 1
ans = 0
mod = 10**9+7
if N == 1:
    ans = 1
else:
    if alist[0]:
        dp[1] = 0
    else:
        dp[1] = 1
    for i in range(2,N+1):
        if alist[i-1]:
            dp.append(0)
        else:
            dp.append((dp[0]+dp[1])%mod)
        dp.popleft()
    ans = dp[-1]
print(ans)


# In[ ]:




