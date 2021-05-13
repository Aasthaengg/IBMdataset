s = list(input())
l = len(s)

ans = 0

for bit in range(2 ** (l-1)):
    f = s[0]
    for i in range(l-1):
        if ((bit >> i) & 1):
            f += '+'
        f += s[i+1]

    ans += sum(map(int, f.split("+")))
print(ans)