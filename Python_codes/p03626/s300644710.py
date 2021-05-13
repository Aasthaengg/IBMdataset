n = int(input())
m = [0]
s1 = list(input())
s2 = list(input())
for i in range(n):
    if s1[i] == s2[i]:
        m.append(1)
    else:
        if i % 2 == 0:
            m.append(2)

p = 10 ** 9 + 7
ans = 1
for i in range(1, len(m)):
    if m[i - 1] == 0:
        if m[i] == 1:
            ans *= 3
        else:
            ans *= 6
    elif m[i - 1] == 1:
        ans *= 2
    else:
        if m[i] == 2:
            ans *= 3
    if ans >= p:
        ans %= p
print(ans)