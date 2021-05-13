N = int(input())
S = [input() for _ in range(N)]

last_A = []
first_B = []
A_B = []
for i in range(N):
    if (S[i][0] == 'B' and S[i][-1] == 'A'):
        A_B.append(S[i])
    elif (S[i][0] == 'B'):
        first_B.append(S[i])
    elif (S[i][-1] == 'A'):
        last_A.append(S[i])

count = 0
for i in S:
    for j in range(len(i) - 1):
        if i[j] == 'A' and i[j + 1] == 'B':
            count += 1


def calc_comb(sb, fa, sbfa):
    if sbfa == 0:
        return min(sb, fa)
    elif sb == 0 and fa == 0:
        return sbfa - 1
    else:
        return sbfa + min(sb, fa)


print(count + calc_comb(len(first_B), len(last_A), len(A_B)))
