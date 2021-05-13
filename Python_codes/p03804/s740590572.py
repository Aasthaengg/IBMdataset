#!/usr/bin/env python
# coding: utf-8

# In[8]:


N,M = map(int, input().split())
A = []
B = []
for _ in range(N):
    A.append(input())
for _ in range(M):
    B.append(input())


# In[11]:


f = False
for h in range(N-M+1):
    for w in range(N-M+1):
        for i in range(M):
            for j in range(M):
                if B[i][j] != A[i+h][j+w]:
                    break
            else:
                continue
            break
        else:
            f = True
            print("Yes")
            break
    else:
        continue
    break
if f != True:
    print("No")


# In[ ]:




