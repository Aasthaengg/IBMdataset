S = input()
i = 1
while True:
    s = S[: - i]
    n = len(s)
    if n % 2 == 0 and s[:n // 2] == s[n // 2:]:
        print(n)
        exit()
    i += 1
