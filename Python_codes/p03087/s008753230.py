N, Q = map(int, input().split())
S = input()
s = [0]*N
A = []
for n in range(N-1):
    if S[n] + S[n+1] == 'AC':
        s[n+1] = s[n] + 1
    else:
        s[n+1] = s[n]
for q in range(Q):
    l, r = map(int, input().split())
    A.append(s[r-1] - s[l-1])
for a in A:
    print(a)