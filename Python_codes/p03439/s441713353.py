N = int(input())
L, R = 0, N
D = (L + R) // 2
pin = ["" for _ in range(N)]
print(0)
dp = input()
pin[0] = dp[:]
if dp != "Vacant":
    print(D)
    F = 0
    for i in range(18):
        s = input()
        pin[D] = s[:]
        if s == "Vacant":
            break
        else:
            if (L - D) % 2 == 0 and pin[D%N] != pin[L%N]:
                R = D
                D = (L + R) // 2
            elif (L - D) % 2 == 0 and pin[D%N] == pin[L%N]:
                L = D
                D = (L + R) // 2
            elif (R - D) % 2 == 0 and pin[D%N] != pin[R%N]:
                L = D
                D = (L + R) // 2
            elif (R - D) % 2 == 0 and pin[D%N] == pin[R%N]:
                R = D
                D = (L + R) // 2
            elif (L - D) % 2 == 1 and pin[D%N] == pin[L%N]:
                R = D
                D = (L + R) // 2
            elif (L - D) % 2 == 1 and pin[D%N] != pin[L%N]:
                L = D
                D = (L + R) // 2
            elif (R - D) % 2 == 1 and pin[D%N] == pin[R%N]:
                L = D
                D = (L + R) // 2
            elif (R - D) % 2 == 1 and pin[D%N] != pin[R%N]:
                R = D
                D = (L + R) // 2
            print(D)