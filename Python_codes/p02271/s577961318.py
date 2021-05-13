n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))
bits = 1
for a in A:
    bits |= bits << a
for m in M:
    print('yes' if (bits >> m) & 1 else 'no')
