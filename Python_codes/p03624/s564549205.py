# -*- coding: utf-8 -*-

S = list(str(input()))

chr_ord = 97

for i in range(26):
    if chr(chr_ord + i) not in S:
        print(chr(chr_ord + i))
        exit()

print('None')