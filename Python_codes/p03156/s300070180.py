N = int(input())
A,B = map(int, input().split())
*P, = map(int, input().split())

P.sort()

c = [0] * 3
for p in P:
    if p <= A:
        c[0] += 1
    elif A < p <= B:
        c[1] += 1
    elif B < p:
        c[2] += 1

print(min(c))