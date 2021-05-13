#!/usr/bin/env python
# coding: utf-8

# In[6]:


N = int(input())
a = list(map(int, input().split()))


# In[8]:


a_set = set(a)
if len(a_set) == 1:
    if sum(a) == 0:
        ans = "Yes"
    else:
        ans = "No"
elif len(a_set) == 2:
    a1,a2 = sorted(a_set)
    if a1 == 0 and N == a.count(a1)*3:
        ans = "Yes"
    else:
        ans = "No"
elif len(a_set) == 3:
    a1,a2,a3 = a_set
    if (a1^a2^a3 == 0) and (a.count(a1)==a.count(a2)==a.count(a3)):
        ans = "Yes"
    else:
        ans = "No"
else:
    ans = "No"
    
print(ans)


# In[ ]:




