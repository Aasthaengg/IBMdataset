N, P = map(int, input().split())
A = [int(x) for x in input().split()]

odd = False
for i in range(N):
    if A[i] % 2 == 1:
        odd = True
        break

if odd:
    print(2**(N-1))
else:
    if P == 0:
        print(2**N)
    else:
        print(0)