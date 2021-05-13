#!/usr/bin/env python
# coding: utf-8

# In[21]:


P = int(input())


# In[22]:


# i_list = list(range(1, P+1))
# p_list = i_list[1:]
# p_list.append(i_list[0])

# # print(i_list, p_list)

# ans = 0
# for i in range(P):
#     ans += i_list[i]%p_list[i]
# print(ans)

# ans = sum(range(1,P))
ans = P*(P-1)//2
print(ans)


# In[ ]:




