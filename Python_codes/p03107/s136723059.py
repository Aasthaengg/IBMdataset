S = input()

ss = []
ans = 0
for i in range(len(S)): ss.append(S[i])

zeros = 0
ones = 0

for i in range(len(ss)):
    if ss[i] == "0":
        zeros += 1
    elif ss[i] == "1":
        ones += 1

ans = 2*min(zeros, ones)
print(ans)
