def main():
    S = [i for i in input()]
    O = S[:]
    K = int(input())
    if len(S) == 1:
        return K // 2
    r = 0
    for i in range(1, len(S)):
        if S[i] == S[i - 1]:
            r += 1
            S[i] = S[i].upper()
    if S[-1] != S[0]:
        return r * K

    S = S + O
    p = 0
    for i in range(len(O), len(S)):
        if S[i] == S[i - 1]:
            p += 1
            S[i] = S[i].upper()
    if S[-1] == S[0]:
        return r + p * (K - 1)
    return (r + p) * (K // 2) + r * (K % 2)
   

print(main())
