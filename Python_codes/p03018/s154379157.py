s = input()
s = s.replace('BC','D')
A_count = 0
ans = 0

for i in s:
    if i == 'A':
        A_count += 1
    elif i == 'B' or i == 'C':
        A_count = 0
    else:
        ans += A_count
print(ans)