D = int(input())
C = [int(i) for i in input().split()]
S = []
for _ in range(D):
    s = [int(i) for i in input().split()]
    S.append(s)

L = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sum = 0
for i in range(D):
    t = int(input())
    s = S[i]
    sum += s[t - 1]
    for j in range(26):
        if j == t - 1:
            L[t - 1] = i + 1
        else:
            sum -= C[j] * (i + 1 - L[j])
    print(sum)
