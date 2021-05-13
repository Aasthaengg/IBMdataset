N, Y = map(int, input().split())
Y /= 1000
total = 0
flag = 0

for A in range(N+1):
    for B in range(N+1):
        C = N - A - B
        if C<0:
            break
        total = 10 * A + 5 * B + C
        if total == Y:
            print(A, B, C)
            flag = 1
            break
    if flag == 1:
        break

if flag == 0:
    print('-1 -1 -1')