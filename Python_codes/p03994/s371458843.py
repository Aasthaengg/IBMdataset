s = input()
k = int(input())

ns = []
for c in s[:-1]:
    if c == 'a':
        ns.append(c)
        continue

    ofstoa = ord('z')+1-ord(c)
    if k >= ofstoa:
        ns.append(chr(ord(c) + ofstoa - 26))
        k -= ofstoa
    else:
        ns.append(c)

last = ord(s[-1])
k = k%26
if last + k > ord('z'):
    ns.append(chr(last + k - 26))
else:
    ns.append(chr(last + k))
print(''.join(ns))
