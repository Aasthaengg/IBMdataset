N = int(input())
SP = [None] * N
for i in range(N):
    SP[i] = input().split() + [i + 1]
    SP[i][1] = int(SP[i][1]) * (-1)

SP.sort(key = lambda x : (x[0], x[1]))
for i in range(N):
    print(SP[i][2])