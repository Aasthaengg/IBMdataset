# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 13:02:30 2020

@author: NEC-PCuser
"""

SX, SY, TX, TY = map(int, input().split())

ans = ""

if TX - SX > 0 and TY - SY > 0:
    first = "R"
    second = "U"
    third = "L"
    forth = "D"
elif TX - SX < 0 and TY - SY > 0:
    first = "L"
    second = "U"
    third = "R"
    forth = "D"
elif TX - SX < 0 and TY - SY < 0:
    first = "L"
    second = "D"
    third = "R"
    forth = "U"
elif TX - SX > 0 and TY - SY < 0:
    first = "R"
    second = "D"
    third = "L"
    forth = "U"

for i in range (TX - SX):
    ans += first
for i in range (TY - SY):
    ans += second
for i in range (TX - SX):
    ans += third
for i in range (TY - SY):
    ans += forth
ans += forth
for i in range (TX - SX + 1):
    ans += first
for i in range (TY - SY + 1):
    ans += second
ans += third
ans += second
for i in range (TX - SX + 1):
    ans += third
for i in range (TY - SY + 1):
    ans += forth
ans += first

print(ans)