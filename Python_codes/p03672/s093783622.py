s = str(input())
while True:
    s = s[:-1]
    n = len(s) // 2
    if s[:n] == s[n:]:
        print(2 * n)
        exit()