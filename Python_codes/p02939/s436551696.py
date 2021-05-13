def main():
    S = input()
    if len(S) == 1:
        return 1
    dp1 = [0] * len(S)
    dp2 = [0] * len(S)
    dp1[0] = 1
    dp2[1] = 1
    if S[0] != S[1]:
        dp1[1] = 2

    for i, s in enumerate(S[1:], 1):
        if s != S[i - 1]:
            dp1[i] = max(dp1[i], dp1[i - 1] + 1)
        dp1[i] = max(dp1[i], dp2[i - 1] + 1)
        dp2[i] = dp1[i - 2] + 1
        if S[i - 1:i + 1] != S[i - 3:i - 1]:
            dp2[i] = max(dp2[i], dp2[i - 2] + 1)
    return max(dp1[-1], dp2[-1])
        

print(main())

