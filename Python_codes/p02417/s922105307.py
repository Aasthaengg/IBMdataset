import sys
a=[0 for _ in range(26)]
for s in sys.stdin:
    for c in s.lower():
        if 'a' <= c <= 'z':
            a[ord(c) - 97] += 1
for i,v in enumerate(a):
    print(chr(i+97) + " : " + str(v))