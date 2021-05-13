a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

max_num = a
min_num = a
if b < min_num:
    min_num = b
if b > max_num:
    max_num = b

if c < min_num:
    min_num = c
if c > max_num:
    max_num = c

if d < min_num:
    min_num = d
if d > max_num:
    max_num = d

if e < min_num:
    min_num = e
if e > max_num:
    max_num = e

if max_num - min_num <= k:
    print('Yay!')
else:
    print(':(')
