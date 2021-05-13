# -*- coding: utf-8 -*-

s = list(input())

tmp_str =""
output=""
start_pos = end_pos = -1


for i in range(len(s)):
    if s[i] == 'A':
        start_pos = i
        break

for i in range(len(s)-1,0,-1):
    if s[i] == 'Z':
        end_pos = i
        break

if end_pos>=0 and start_pos>=0:
    length = end_pos - start_pos + 1
else:
    length = 0

print(length)