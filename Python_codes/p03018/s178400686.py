s = input()
s = s.replace('BC', '1')
ans = 0
a = 0
for s_ in s:
    if s_ == 'A':
        a += 1
    elif s_ == '1':
        ans += a
    else:
        a = 0
print(ans)
