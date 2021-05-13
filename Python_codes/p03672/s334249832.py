S = input()

for i in range(1, len(S)):
    s = S[:-i]
    n = len(s)

    if n % 2 == 0 and s[:n // 2] == s[-n // 2:]:
        print(n)
        break