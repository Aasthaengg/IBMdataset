n = int(input())
T = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
p = 10 ** 9 + 7

B = [10**9] * n

h = 0

for i, t in enumerate(T):
    if h < t:
        B[i] = 1
        h = t
    else:
        B[i] = h

h = 0

for i, a in zip(range(n-1, -1, -1), A[::-1]):
    if h < a:
        if a > T[i] or (B[i] == 1 and a != T[i]):
            print(0)
            exit(0)
        B[i] = 1
        h = a
    elif B[i] == 1 and T[i] > a:
        print(0)
        exit(0)
    elif B[i] > h:
        B[i] = h

ans = 1

for b in B:
    ans *= b
    ans %= p

print(ans)