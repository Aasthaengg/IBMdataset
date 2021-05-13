N = int(input())
S = input()
i = 0
j = N - 1
ans = 0
while i < j:
    while i < N and S[i] == 'R':
        i += 1
    while j > 0 and S[j] == 'W':
        j -= 1
    if i >= j:
        break
    ans += 1
    i += 1
    j -= 1
print(ans)
