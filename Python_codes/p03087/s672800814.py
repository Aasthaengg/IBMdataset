n, q = map(int, input().split())
S = input()
CS = [0]
cur = 0
for i in range(1, n):
    if S[i-1] + S[i] == 'AC':
        cur += 1
        CS.append(cur)
    else:
        CS.append(cur)

for _ in range(q):
    l, r = map(int, input().split())
    print(CS[r-1] - CS[l-1])

