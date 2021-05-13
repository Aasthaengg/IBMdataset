S = [input() for _ in range(3)]
i = [0,0,0]
t = 0
while True:
    if i[t] == len(S[t]):
        print(chr(t+ord('A')))
        exit()
    i[t] += 1
    t = ord(S[t][i[t]-1]) - ord('a')
