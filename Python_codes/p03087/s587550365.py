
N, Q = map(int, input().split())
S = input().rstrip('\n')
count = [0]*(N+2)

for i in range(N-1):
    if S[i] == 'A' and S[i+1] == 'C':
        count[i+1] = 1

#累積和
for i in range(1, N+1):
    count[i] += count[i-1]

for _ in range(Q):
    l, r = map(int, input().split())
    print(count[r-1] - count[l-1])


