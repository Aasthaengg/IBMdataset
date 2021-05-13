#!/usr/bin/env python
# coding: utf-8

# In[43]:


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


# In[45]:


# if sum(A) < sum(B):
#     ans = -1
# else:
#     diff_plus = sorted([B[i]-A[i] for i in range(N) if B[i]-A[i]>0])
#     diff_minus = sorted([A[i]-B[i] for i in range(N) if A[i]-B[i]>0],reverse=True)
#     if len(diff_plus) > 0:
#         j = 0
#         cnt = len(diff_plus)
#         for i,x in enumerate(diff_plus):
#             while sum(diff_minus[:j+1]) < x:
#                 j += 1
#             diff_minus[j] = sum(diff_minus[:j+1])-x
#             for k in range(j):
#                 diff_minus[k] = 0
#         ans = j+1+cnt
#     else:
#         ans = 0
# print(ans)


# In[47]:


husoku = [a-b for a, b in zip(A, B) if a-b < 0]
amari = [a-b for a, b in zip(A, B) if a-b > 0]
amari.sort(reverse=True)
 
H = abs(sum(husoku))
if len(husoku) == 0:
    ans = 0
elif H > sum(amari):
    ans = -1
else:
    for i, a in enumerate(amari, start=1):
        H -= a
        if H <= 0:
            ans = len(husoku) + i
            break
print(ans)


# In[ ]:




