s = list(str(input()))
t = list(str(input()))

asc_s = sorted(s)
desc_t = sorted(t, reverse=True)

print("Yes" if ''.join(asc_s) < ''.join(desc_t) else "No")