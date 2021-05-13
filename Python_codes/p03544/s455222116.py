N=int(input())
if N == 1:
    print(1)
    exit()

l0=2
l1=1
for i in range(2,N+1):
    L = l1 + l0
    l0 = l1
    l1 = L

print(L)

