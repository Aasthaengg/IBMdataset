N = int(input())
S = input()

e = 0
ans = w = S.count('E')
for i in S:
    if i == 'E':
        w -= 1
    else:
        e += 1
    ans = (min(ans, e+w))

print(ans)