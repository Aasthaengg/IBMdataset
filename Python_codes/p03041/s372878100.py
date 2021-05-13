n, k = map(int, input().split())
s = list(input())

if s[k-1].isupper():
    s[k-1] = s[k-1].lower()
else:
    s[k-1] = s[k-1].upper()

print(''.join(s))
