# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 17:00:46 2020

@author: saito
"""

# %% import phase

# %% define phase

# %% input phase
N = int(input())
S = [0]*N
for i in range(N):
    S[i] = input()

# %% process phase
C = [0]*4
rslt = ['AC', 'WA', 'TLE', 'RE']
for i in range(4):
    C[i] = S.count(rslt[i])

# %%output phase
for i in range(4):
    print(rslt[i]+' '+'x'+' '+str(C[i]))