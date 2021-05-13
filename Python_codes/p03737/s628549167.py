s = input().split()

res = ''
for i in s:
    res += chr(ord(i[0])-0x20)
print(res)