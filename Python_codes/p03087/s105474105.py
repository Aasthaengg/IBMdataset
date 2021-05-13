#!/usr/bin/env python
# coding: utf-8

# In[15]:


N,Q = map(int, input().split())
S = list(input())
mylist = [0]
cnt = 0
for i in range(1,len(S)):
    if S[i-1] == "A" and S[i] == "C":
        cnt += 1
    mylist.append(cnt)
for _ in range(Q):
    l,r = map(int, input().split())
    ans = mylist[r-1] - mylist[l-1]
    print(ans)


# In[ ]:




