S = input()
n = len(S)
res = 10 ** 6
for i in range(n-2):
    s = int(S[i:i+3])
    res = min(res, abs(s - 753))
print(res)