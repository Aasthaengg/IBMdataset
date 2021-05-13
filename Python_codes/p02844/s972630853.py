N = int(input())
S = input()

ans = 0
for i in range(10):
    idx0 = S[: N - 2].find(str(i))
    if idx0 != -1:
        for j in range(10):
            idx1 = S[idx0 + 1 : N - 1].find(str(j))
            if idx1 != -1:
                for k in range(10):
                    idx2 = S[idx0 + idx1 + 2 :].find(str(k))
                    if idx2 != -1:
                        ans += 1

print(ans)

