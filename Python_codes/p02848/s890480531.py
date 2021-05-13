n = int(input())
for i in input():
    if ord(i)+n>90: print(chr(64+ord(i)+n-90), end = '')
    else: print(chr(ord(i)+n), end = '')