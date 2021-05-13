s = input()
res = 0
st = s[0]

for v in s:
    if st != v:
        res += 1
        st = v
print(res)