s = input()
s = s.replace('BC', 'X')

cnt = 0
ans = 0

# AとXが連続している限り、Xより左のAは右にスキップしていける
for x in s:
    if x == 'A':
        cnt += 1
    elif x == 'X':
        ans += cnt
    else:
        cnt = 0

print(ans)