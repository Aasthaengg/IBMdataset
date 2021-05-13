# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 17:18:33 2020

@author: NEC-PCuser
"""

N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

score = 0
your_hand = [-1] * N
# グー 0 チョキ 1 パー 2
score_dict = {"r":P, "s":R, "p":S}


for i in range(len(T)):
    if T[i] != your_hand[i - K]:
        score += score_dict[T[i]]
        your_hand[i] = T[i]

print(score)