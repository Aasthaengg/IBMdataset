n = int(input())
S = input().split()
S.append(None)

q = int(input())
T = input().split()

cnt = 0

for i in range(q):
    sentry = T[i]
    S[n] = sentry
    j = 0
    while S[j] != sentry:
        j += 1
    if j != n:
        cnt += 1

print(cnt)