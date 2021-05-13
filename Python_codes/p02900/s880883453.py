#!/usr/bin/env python
# coding: utf-8

# In[18]:


import math


# In[23]:


A,B = map(int, input().split())


# In[24]:


# #nの約数を全て求める
# def divisor(n): 
#     i = 1
#     table = []
#     while i * i <= n:
#         if n%i == 0:
#             table.append(i)
#             table.append(n//i)
#         i += 1
#     table = list(set(table))
#     return table


# In[29]:


# def func():
#     mylist = []
#     tmp = 1
#     if A<=B:
#         for x in divisor(A):
#             if B%x==0 and math.gcd(tmp,x)==1:
#                 mylist.append(x)
#                 tmp *= x
#     else:
#         for x in divisor(B):
#             if A%x==0 and math.gcd(tmp,x)==1:
#                 mylist.append(x)
#                 tmp *= x
# #     print(mylist)
#     print(len(mylist))
# if __name__=="__main__":
#     func()


# In[30]:


gcd=math.gcd(A,B)
m = gcd
pf = {}
for i in range(2, int(m**0.5)+1):
    while m % i == 0:
        pf[i] = pf.get(i, 0)+1
        m //= i
if m > 1:
    pf[m] = 1
print(len(pf)+1)


# In[ ]:




