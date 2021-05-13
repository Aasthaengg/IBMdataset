S = list(input())
l = len(S)

ans = 0

for bit in range(1 << (l-1)):
    # print(bit)
    f = S[0]
    for i in range(l-1):
        if bit & (1 << i):
            f += "+"
        f += S[i+1]

    ans += sum(map(int, f.split("+")))
print(ans)
