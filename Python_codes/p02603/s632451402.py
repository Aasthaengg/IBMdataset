N = int(input())
A = [int(i) for i in input().split()]

W = [0] * N

for i in range(1, N):
    W[i] = A[i] - A[i - 1]
B = [0]
for w in W:
    if not w == 0:
        B.append(w)
l = len(B)
money = 1000
kabu = 0
value = A[0]
for i in range(l):
    value += B[i]
    if (i == l - 1) or (B[i] > 0 and B[i + 1] < 0):
        money += kabu * value
        kabu = 0
    elif (i == 0 and B[i + 1] > 0) or (B[i] < 0 and B[i + 1] > 0):
        n = money // value
        money -= n * value
        kabu += n

print(money)
