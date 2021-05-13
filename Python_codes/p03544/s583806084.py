N = int(input())
L0 = 2
L1 = 1
if N == 1:
    print(L1)
    exit()

for i in range(1,N):
    res = L0 + L1
    L0 = L1
    L1 = res

print(res)