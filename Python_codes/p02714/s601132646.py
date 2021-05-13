N = int(input())
S = input()

nr = 0
ng = 0
nb = 0

for i in S:
    if i == 'R':
        nr += 1
    elif i == 'G':
        ng += 1
    elif i == 'B':
        nb += 1
    else:
        raise RuntimeError

ans = nr * ng * nb

for j in range(N):
    for i in range(j):
        k = 2 * j - i
        if k < N:
            if S[i] == S[j]: continue
            if S[i] == S[k]: continue
            if S[j] == S[k]: continue
            ans -= 1

print(ans)
