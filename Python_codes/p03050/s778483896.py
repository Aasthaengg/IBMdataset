#!/usr/bin/env python
# coding: utf-8

# In[79]:


N = int(input())


# In[80]:


def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


# In[82]:


if N < 3:
    print(0)
else:
    mylist = make_divisors(N)
    idx = len(mylist)//2
    ans = 0
    for x in mylist[idx:]:
        if N//(x-1) == N%(x-1):
            ans += x-1
    print(ans)


# In[ ]:




