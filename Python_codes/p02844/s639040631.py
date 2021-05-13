N = int(input())
S = input()
S1 = S
Comb = 0
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            S = S1
            a, b, c = map(str, [i, j, k])
            if S.find(a) != -1:
                S = S[S.find(a)+1::]
                if S.find(b) != -1:
                    S = S[S.find(b)+1::]
                    if S.find(c) != -1:
                        Comb += 1
print(Comb)