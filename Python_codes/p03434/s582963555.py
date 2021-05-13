"""Boot-camp-for-Beginners_Easy010_B_Toll-Gates_29-August-2020.py"""
import numpy as np

N = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)

Alice = [a[i] for i in range(0, len(a), 2)]
Bob = [a[i] for i in range(1, len(a), 2)]
#print(Alice)
#print(Bob)

s_max = 0
for i in range(len(Alice)):
    s_max += Alice[i]
s_min = 0
for i in range(len(Bob)):
    s_min += Bob[i]
#print(s_max)
#print(s_min)
print(s_max-s_min)
