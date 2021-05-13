#!/usr/bin/env python
# coding: utf-8

# In[1]:


N, K = map(int, input().split())


# In[2]:


A = [int(x) for x in input().split()]


# In[11]:


ones = [0] * 40
for a in A:
    s = format(a, '040b')
    for i in range(40):
        ones[i] += int(s[i])
    


# In[12]:


kb = format(K, '040b')
flag = False
ret = []
for i in range(40):
    if flag:
        if ones[i] >= N / 2:
            ret.append(0)
        else:
            ret.append(1)
    else:
        if kb[i] == '0':
            ret.append(0)
        else:
            if ones[i] >= N / 2:
                ret.append(0)
                flag = True
            else:
                ret.append(1)


# In[13]:


ans = 0
for i in range(40):
    if ret[i] == 0:
        ans += 2 ** (39 - i) * ones[i]
    else:
        ans += 2 ** (39 - i) * (N - ones[i])


# In[14]:


print(ans)


# In[ ]:





# In[ ]:





# In[ ]:




