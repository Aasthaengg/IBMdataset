S = input().rstrip()
L = len(S)
res = float("inf")
for i in range(L-2):
    res = min(abs(int(S[i:i+3]) - 753), res)
print(res)