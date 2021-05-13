L1 = list(map(int,input().split()))
L2 = list(set(L1))
print(2 * sum(L2) - sum(L1))