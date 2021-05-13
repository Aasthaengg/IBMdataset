n = (int)(input())
s = input()

ret = ""
retc = ''
for i in range(len(s)):
    c = ord(s[i])
    if c + n > ord('Z'):
        retc = c + n - ord('Z') + ord('A') - 1
    else:
        retc = c + n
    ret += chr(retc)

print("{}".format(ret))