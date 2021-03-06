#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


H, W = map(int, input().split())
S = np.ones((H, W), dtype=np.bool)
for i in range(H):
    S[i] = [s == "." for s in input()]


# In[3]:


up = np.zeros((H, W), dtype=np.int16)
down = np.zeros((H, W), dtype=np.int16)
left = np.zeros((H, W), dtype=np.int16)
right = np.zeros((H, W), dtype=np.int16)

# up
up[0, :] = S[0, :]
for h in range(1, H):
    up[h, :] = up[h - 1, :] + 1
    up[h, :] *= S[h, :]

# down
down[H - 1, :] = S[H - 1, :]
for h in reversed(range(0, H - 1)):
    down[h, :] = down[h + 1, :] + 1
    down[h, :] *= S[h, :]

# left
left[:, 0] = S[:, 0]
for w in range(1, W):
    left[:, w] = left[:, w - 1] + 1
    left[:, w] *= S[:, w]

# right
right[:, W - 1] = S[:, W - 1]
for w in reversed(range(0, W - 1)):
    right[:, w] = right[:, w + 1] + 1
    right[:, w] *= S[:, w]

ans = np.max(up + down + left + right - 3)
print(ans)


# In[ ]:




