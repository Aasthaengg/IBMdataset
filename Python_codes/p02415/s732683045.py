st = raw_input()
ans = ''
for ch in st:
    if ch.islower():
        ans += ch.upper()
    elif ch.isupper():
        ans += ch.lower()
    else:
        ans += ch
print ans