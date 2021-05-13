N = list(map(int, list(input())))[::-1]
dp0 = [float('inf')] * (len(N)+1)
dp1 = [float('inf')] * (len(N)+1)
dp0[0] = 0
dp1[0] = 1
for i in range(len(N)):
    dp0[i+1] = min(dp0[i] + N[i], dp1[i] + 10 - N[i])
    dp1[i+1] = min(dp0[i] + N[i] + 1, dp1[i] + 9 - N[i])
print(dp0[-1])
