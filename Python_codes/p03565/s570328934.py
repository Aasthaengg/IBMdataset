#!/usr/bin/env python
# coding: utf-8

# In[29]:


Sdash = input()
T = input()


# In[30]:


length_S = len(Sdash)
length_T = len(T)
if length_S >= length_T:
    for i in range(length_S-length_T+1):
        for j in range(length_T):
            if Sdash[j+length_S-length_T-i] != T[j] and Sdash[j+length_S-length_T-i] != "?":
                break
        else:
            ans = Sdash[:length_S-length_T-i]+T+Sdash[length_S-i:]
            ans = [x if x != "?" else "a" for x in ans]
            print("".join(ans))
            break
    else:
        print("UNRESTORABLE")
else:
    print("UNRESTORABLE")


# In[ ]:




