import sys

K = int(input())
A, B = map(int, input().split())

if K == 1:
    print('OK')
    sys.exit()

n = 1
while True:
    m = K * n
    if A <= m <= B:
        print('OK')
        sys.exit()

    if n == B:
        break

    n += 1

print('NG')
