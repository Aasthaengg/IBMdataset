S = input()
sumW = sum([i for i in range(len(S)) if S[i] == 'W'])
n = S.count('W')
newW = n * (n - 1) // 2
print(sumW - newW)