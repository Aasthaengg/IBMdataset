#!/usr/bin/env python
# coding: utf-8

# In[12]:


S = input()


# In[17]:


length = len(S)
if length == 1:
    print(1)
elif length == 2:
    if S[0] == S[1]:
        print(1)
    else:
        print(2)
else:
    dp = [0]*length
    dp[0] = 1
    if S[0] == S[1]:
        dp[1] = 1
    else:
        dp[1] = 2
    if S[0] != S[1] and S[1] != S[2]:
        dp[2] = 3
    else:
        dp[2] = 2

    for i in range(3, length):
#         print(dp)
        if S[i-1] == S[i]:
            dp[i] = dp[i-3] + 2
        else:
            dp[i] = dp[i-1] + 1
    print(dp[-1])


# In[5]:





# In[ ]:




