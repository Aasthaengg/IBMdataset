#!/usr/bin/env python
# coding: utf-8

# In[14]:


N,M = map(int, input().split())
A = list(map(int, input().split()))
BC = []
for _ in range(M):
    BC.append(list(map(int, input().split())))


# In[15]:


bc_sorted = sorted(BC, key=lambda x:x[1], reverse=True)
mylist = [a for a in A]
for i in range(M):
    mylist += [bc_sorted[i][1]]*bc_sorted[i][0]
    if len(mylist) > N*2:
        break
ans = sorted(mylist, reverse=True)[:N]
print(sum(ans))


# In[ ]:




