N,P = map(int, input().split())
A = list(map(int, input().split()))
in_odd = False
for i in range(N):
    if A[i]%2:
        in_odd = True
        break
if not in_odd:
    if P:
        print(0)
    else:
        print(2**N)
else:
    print(2**(N-1))