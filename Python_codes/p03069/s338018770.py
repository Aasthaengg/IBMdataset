N = int(input())
S = input()
if len(set(S)) == 1:
    print(0)
    exit()

sum_blacks = [0] * N
if S[0] == "#":
    sum_blacks[0] += 1
for i in range(1, N):
    if S[i] == "#":
        sum_blacks[i] = sum_blacks[i - 1] + 1
    else:
        sum_blacks[i] = sum_blacks[i - 1]
ans = float('inf')
ans = min(ans, sum_blacks[-1])
ans = min(ans, N - sum_blacks[-1])
for i in range(N):
    l_blacks = sum_blacks[i]
    l_whites = i + 1 - l_blacks
    r_blacks = sum_blacks[-1] - l_blacks
    r_whites = N - l_blacks - l_whites - r_blacks
    ans = min(ans, l_blacks + r_whites)
print(ans)