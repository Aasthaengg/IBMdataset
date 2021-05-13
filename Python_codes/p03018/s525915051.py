s = input()
s = s.replace('BC', 'T')
a_count = 0
ans = 0
for c in s:
    if c == 'A':
        a_count += 1
    elif c == 'T':
        ans += a_count
    else:
        a_count = 0
print(ans)
