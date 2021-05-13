#!/usr/bin/env python
# coding: utf-8

# In[5]:


# S = input()


# In[6]:


# S_tail = list(S)
# S_tail.append("R")
# group = []
# tmp = []
# count = 0
# while count < len(S):
#     tmp.append(S_tail[count])
#     if S_tail[count] != S_tail[count+1]:
#         group.append(tmp)
#         tmp = []
#     count += 1


# In[7]:


# print(group)
# group_cnt = []
# count2 = 0
# for i in range(0,len(group),2):
# #     print("aaa")
#     if count2%2 == 0:
# #         print(group[i], len(group[i])//2)
#         count2 += len(group[i])
#         r_tmp = len(group[i])//2
#     else:
# #         print(group[i], len(group[i])//2+1)
#         count2 += len(group[i])
#         r_tmp = len(group[i])//2+1
        
#     if count2%2 == 0:
# #         print(group[i+1], len(group[i+1])//2)
#         count2 += len(group[i+1])
#         l_tmp = len(group[i+1])//2
#     else:
# #         print(group[i+1], len(group[i+1])//2+1)
#         count2 += len(group[i+1])
#         l_tmp = len(group[i+1])//2+1
# #     print(r_tmp, l_tmp)
#     group_cnt.append(r_tmp+l_tmp)
#     group_cnt.append(len(group[i])+len(group[i+1]) - (r_tmp+l_tmp))
#     r_tmp = 0
#     l_tmp = 0
# # print(group_cnt)


# In[8]:


# ans = [[0]*(len(group[i])-1)+[group_cnt[i]] if i%2 == 0 else [group_cnt[i]]+[0]*(len(group[i])-1) for i in range(len(group))]
# ans2 = []
# for i in range(len(ans)):
#     ans2 += ans[i]
# print(" ".join(list(map(str,ans2))))


# In[12]:


def main():
  s = input()
  ans = [1] * len(s)
  for i in range(len(s)-2):
    if s[i]=='R' and s[i+1]=='R':
      ans[i+2] += ans[i]
      ans[i] = 0
#     print(ans)
  for i in range(len(s)-1, 1, -1):
    if s[i]=='L' and s[i-1]=='L':
      ans[i-2] += ans[i]
      ans[i] = 0
#     print(ans)
  print(" ".join(map(str, ans)))
  
if __name__ == '__main__':
  main()


# In[ ]:




