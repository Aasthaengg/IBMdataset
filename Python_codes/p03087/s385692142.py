N, Q = map(int, input().split())
S = input()

C = [0 for _ in range(N)]
count = 0
prev = S[0]
for i, s in enumerate(S[1:]):
    now = s
    if prev + now == 'AC':
        count += 1
    C[i+1] = count
    prev = now
C

for j in range(Q):
    l, r = map(int, input().split())
    print(C[r-1] - C[l-1])