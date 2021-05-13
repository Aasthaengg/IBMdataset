S = list(map(int, list(input())))
ans = ""
for bit in range(2**3):
    temp = S[0]

    for i in range(3):

        if bit & (1<<i):
            temp +=S[i+1]
        else:
            temp -= S[i+1]

    if temp == 7:
        for i in range(3):
            ans += str(S[i])

            if bit & (1 << i):
                ans += "+"
            else:
                ans += "-"
        ans += str(S[3]) + "=7"
        print(ans)
        break

