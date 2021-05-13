s = input()
ok = True
for c in "abc":
    ok &= c in s

print('Yes' if ok else 'No')
