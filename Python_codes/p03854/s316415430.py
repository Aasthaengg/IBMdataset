s = input()
s = s[::-1]
t = ['maerd', 'remaerd', 'esare', 'resare']

while s:
    l = len(s)
    for i in[7,6,5]:
        while s[:i:] in t:
            s = s[i::]
    if l == len(s):
        print('NO')
        exit()
print('YES')