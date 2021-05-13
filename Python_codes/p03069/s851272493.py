N = int(input())
S = input()
w = S.count('.')
b, i = 0, 0
ans = w
for s in S:
    if s == '.':
        w -= 1
    else:
        b += 1
    ans = min(ans, w+b)
print(ans)
