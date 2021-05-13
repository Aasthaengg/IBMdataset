N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))

c0 = 0
c1 = 0
c2 = 0

for i in range(N):
    if P[i] <= A:
        c0 += 1
    elif A + 1 <= P[i] <= B:
        c1 += 1
    else:
        c2 += 1

print(min(c0, c1, c2))
