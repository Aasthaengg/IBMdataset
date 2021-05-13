n = int(input())
s = input()
if n % 2 == 1: 
    print('No')
    exit()
h = n // 2
a = s[:h]
b = s[h:n]
if a == b: print('Yes')
else: print('No')