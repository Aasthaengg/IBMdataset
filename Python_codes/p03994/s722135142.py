s = [ord(i) for i in input()]
K = int(input())

ret = []
for c in s[:-1] :
    if c == 97 :
        ret.append('a')
        continue
        
    if c + K > 122 :
        ret.append('a')
        K -= 123 - c
    else :
        ret.append(chr(c))
        
K %= 26
ret.append(chr((s[-1] + K - 97) % 26 + 97))
        
print(''.join(ret))