
N = int(input())

A = [int(input()) for _ in range(N)]

res = 0
last = N
for i,a in zip(reversed(range(N)), reversed(A)):
    j = i-a
    if j > last or j < 0:
        res = -1
        break
    elif j < last:
        last = j
        res += a

print(res)
