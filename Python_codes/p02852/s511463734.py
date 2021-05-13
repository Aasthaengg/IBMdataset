
N, M = map(int, input().split())
S = input()

i = N
ans = []
while i > 0:
    for j in reversed(range(1, M + 1)):
        if i - j >= 0 and S[i - j] == "0":
            ans.append(j)
            i -= j
            break
    else:
        ans = []
        break

if ans:
    print(*ans[::-1])
else:
    print(-1)
