S = input()
N = len(S)
alr = set()

tmp = ""
prev = ""
i = 0
ans = 0
while i < N:
    tmp += S[i]
    if tmp != prev:
        prev = tmp
        ans += 1
        alr.add(tmp)
        tmp = ""
    i += 1

print(ans)

