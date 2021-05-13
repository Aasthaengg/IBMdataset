N, Q = map(int, input().split())
S = input()
s = [0]*(N+1)
for n in range(N):
    if n + 1 < N and S[n] == 'A' and S[n+1] == 'C':
        s[n+1] = s[n] + 1
    else:
        s[n+1] = s[n]
A = []
for q in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    A.append(s[r]-s[l])
for a in A:
    print(a)