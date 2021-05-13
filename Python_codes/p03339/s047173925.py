N = int(input())
S = input()

i = S[1:].count('E')
ans = [i]

for n in range(N):
    if n == 0:
        continue

    if S[n] == 'E':
        i -= 1

    if S[n - 1] == 'W':
        i += 1
    ans.append(i)

print(min(ans))