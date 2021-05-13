S = input()
N = len(S)
ans = [0] * N
i = 0
while i < N:
    if i == N-1:
        ans[N-1] += 1
        break
    count = 1
    while S[i + count] == S[i]:
        count += 1
        if count == N - i:
            break
    if S[i] == 'R':
        ans[i + count - 1] += (count + 1) // 2
        ans[i + count] += count // 2
    else:
        ans[i] += (count + 1) // 2
        ans[i - 1] += count // 2
    i += count
print(*ans)