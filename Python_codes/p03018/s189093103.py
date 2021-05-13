S = input()
S = S.replace('BC', '>')

ans = 0
a_count = 0
for s in S:
    if s == 'A':
        a_count += 1

    elif s == '>':
        ans += a_count

    else:
        a_count = 0

print(ans)
