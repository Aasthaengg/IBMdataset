n, q = map(int, input().split())
S = input()
cum = [0 for _ in range(n)]
for i in range(1, n):
    if S[i-1:i+1] == 'AC':
        cum[i] += cum[i-1] + 1
    else:
        cum[i] = cum[i-1]
for _ in range(q):
    l, r = map(int, input().split())
    print(cum[r-1] - cum[l-1])