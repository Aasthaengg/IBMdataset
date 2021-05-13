L = list(map(int, input().split()))

sub = L[1] % L[0]

if sub == 0:
    print(L[0]+L[1])
else:
    print(L[1]-L[0])