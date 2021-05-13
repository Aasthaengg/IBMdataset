##############################################
import sys
N, M = list(map(int, input().split()))
digits = [-1] * N
for _ in range(M):
    s, c = list(map(int, input().split()))
    s -= 1

    if digits[s] == -1 or (digits[s] != 1 and digits[s] == c):
        digits[s] = c
    else:
        print(-1)
        sys.exit(0)

if digits == [-1]:
    print(0)
    sys.exit(0)
    
if digits[0] == 0 and N != 1:
    print(-1)
    sys.exit(0)


n = 0
base = 1
for i in reversed(range(N)):
    if digits[i] != -1:
        n += base * digits[i]
    elif i == 0 and digits[i] == -1:
        n += base
    base *= 10

print(n)
