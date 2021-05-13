N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if sum(A) < sum(B):
    print(-1)
    exit()

S = [b - a for a, b in zip(A, B) if a < b]

if sum(S) == 0:
    print(0)
    exit()

T = sorted([a - b for a, b in zip(A, B) if a > b], key=lambda x: -x)

cnt = 0
tmp = sum(S)
for t in T:
    tmp -= t
    cnt += 1

    if tmp <= 0:
        break

if tmp > 0:
    print(-1)
    exit()

print(len(S) + cnt)
