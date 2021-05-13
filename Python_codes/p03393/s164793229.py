import sys
s = input()

if len(s) < 26:
    for i in range(ord('a'), ord('z')+1):
        if not chr(i) in s:
            print(s+chr(i))
            break
elif s == 'zyxwvutsrqponmlkjihgfedcba':
    print(-1)
else:
    a = set()
    for i in range(26):
        a.add(s[25-i])
        for j in sorted(a):
            if s < s[:25-i]+j:
                print(s[:25-i]+j)
                sys.exit()
