N = int(input())

P = 1

for i in range(2,N+1):
    P = P*i
    P = P % (10 ** 9 + 7)

print(P)
