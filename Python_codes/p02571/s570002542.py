S, T = input(), input()

ret = len(T)


# burst force
for st in range(0, len(S)-len(T) + 1):

    diff = 0

    for idx in range(0, len(T)):
        if S[st + idx] != T[idx]:
            diff += 1

    ret = min(ret, diff)

print('{}'.format(ret))

