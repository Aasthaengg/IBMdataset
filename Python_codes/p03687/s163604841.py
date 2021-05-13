#!/usr/bin/env python
# coding: utf-8

# In[24]:


from collections import Counter


# In[34]:


s = input()


# In[36]:


mylist = [x for x,c in sorted(Counter(s).items(), key=lambda x: x[1], reverse=True)]
ans = len(s)
for w in mylist:
    myword = s
    cnt = 0
    while len(set(myword)) > 1 and cnt <= ans:
        cnt += 1
        tmp = []
        for i in range(len(myword)-1):
            if myword[i] == w or myword[i+1] == w:
                tmp.append(w)
            else:
                tmp.append(myword[i])
        myword = tmp
    ans = min(cnt, ans)
#     print(myword)
print(ans)


# In[ ]:




