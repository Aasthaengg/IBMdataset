s = input()
n = len(s) - 1
ans = 0

for i in range(2 ** n):
    l = s[0]
    for j in range(n):
        if (i >> j) & 1 == 1:
            l += '+'
        l += s[j + 1]
    ans += sum(map(int, l.split('+')))

print(ans)