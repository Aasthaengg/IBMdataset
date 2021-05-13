N = int(input())
S = input()

i = S[1:].count('E')
r = [i]

for n in range(1, N):
    if S[n] == 'E':
        i -= 1

    if S[n - 1] == 'W':
        i += 1
    r.append(i)

print(min(r))