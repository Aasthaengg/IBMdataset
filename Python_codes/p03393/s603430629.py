S = input()

if len(S) < 26:
    st = set(S)
    for c in range(26):
        if not chr(ord('a') + c) in st:
            S += chr(ord('a') + c)
            break
    print(S)
else:
    i = len(S) - 1
    while i - 1 >= 0 and ord(S[i]) < ord(S[i - 1]):
        i -= 1
    if i == 0:
        print(-1)
    else:
        next_chr = ord(S[i - 1]) - ord('a')
        st = set(S[i:])
        for c in range(next_chr + 1, 26):
            if chr(ord('a') + c) in st:
                print(S[:i - 1] + chr(ord('a') + c))
                break