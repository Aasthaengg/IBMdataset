N = list(input())

M = []

M.append(N[0])
M.append(str(len(N) - 2))
M.append(N[-1])

date = ''.join(M)
print(date)