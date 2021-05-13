#coding: utf-8

s = input()
for i in range(len(s)):
    if ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z'):
        print(chr(ord(s[i])-32), end='')
    elif ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z'):
        print(chr(ord(s[i])+32), end='')
    else:
        print(s[i], end='')
print("")
