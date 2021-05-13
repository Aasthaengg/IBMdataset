from itertools import accumulate
n = int(input())
a = list(map(int,input().split()))
b = list(accumulate(a))
a_sum = sum(a)
dn = float("inf")


for i in range(n-1):
    dn = min(abs(a_sum - 2*b[i]) ,dn)
print(dn)