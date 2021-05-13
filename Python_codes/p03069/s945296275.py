n = int(input())
S = list(input())

w = S.count('.')
b = 0
ans = w+b

for i in range(n):
    if S[i] == '.':
        w -= 1
    else:
        b += 1
    ans = min(ans, w+b)

print(ans)
