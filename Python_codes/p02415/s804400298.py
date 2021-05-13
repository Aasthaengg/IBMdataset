c_dif = ord('A')-ord('a')
s = input()
for c in s:
    if ord('a')<= ord(c) and ord(c) <= ord('z'): 
        print(chr(ord(c)+c_dif) ,end='')
    elif ord('A')<= ord(c) and ord(c) <= ord('Z'): 
        print(chr(ord(c)-c_dif) ,end='')
    else:
        print(c, end='')
print()