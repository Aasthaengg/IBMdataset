#!/usr/bin/env python
# coding: utf-8

# In[27]:


S = input()


# In[28]:


ZtoA = "zyxwvutsrqponmlkjihgfedcba"
diff = sorted(list(set(ZtoA)^set(S)))
if len(S) < 26:
    print(S+diff[0])
else:
    if S == ZtoA:
        print(-1)
    else:
        for i in range(25):
            if S[i] < S[i+1]:
                k = i
        a = "z"
        for i in range(k+1,26):
            if S[k] < S[i]:
                a = min(a, S[i])
        print(S[:k]+a)


# In[ ]:




