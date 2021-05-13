N, Q = map(int, input().split())
S = input()
S = S.replace("AC", "XX")
acc = [0] * (N + 1)
i = 0
while i < N:
    if S[i] == "X":
        acc[i + 2] = 1 
        i += 2
    else:
        i += 1
for i in range(1, N + 1):
    acc[i] += acc[i - 1]

for i in range(Q):
    l, r = map(int, input().split())
    print(acc[r] - acc[l])