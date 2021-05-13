N = int(input())
S = input()
x = S.count('E')
ans = x
for s in S:
    if s == 'E':
        x -= 1
        if ans > x:
            ans = x
    else:
        x += 1
print(ans)
