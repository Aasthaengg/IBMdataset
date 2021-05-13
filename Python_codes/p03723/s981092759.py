#!/usr/bin/env python
# coding: utf-8

# In[20]:


A,B,C = map(int, input().split())


# In[22]:


A_ = A
B_ = B
C_ = C

ans = 0
while True:
    if A_%2 != 0 or B_%2 != 0 or C_%2 != 0:
        print(ans)
        break
    else:
        A_tmp = B_//2 + C_//2
        B_tmp = A_//2 + C_//2
        C_tmp = A_//2 + B_//2
        A_ = A_tmp
        B_ = B_tmp
        C_ = C_tmp
        ans += 1
#         print(A_,B_,C_)
        if A_ == A and B_ == B and C_ == C:
            print(-1)
            break


# In[ ]:




