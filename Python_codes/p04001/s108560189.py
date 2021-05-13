S = input()
answer = 0
for bit in range(2 ** (len(S) - 1)):
    f = S[0]
    for i in range(len(S) - 1):
        if bit & (1 << i):
            f += '+'
        f += S[i + 1]
    answer += sum(map(int, f.split('+')))
print(answer)
