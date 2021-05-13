S = input()
N = len(S)
ans = 0

for n in range(1 << N-1):
    s = S
    cnt = 0
    for i in range(N-1):
        if (n >> i) & 1 == 1:
            s = s[:i+cnt+1] + "+" + s[i+cnt+1:]
            cnt += 1
    ans += eval(s)

print(ans)
