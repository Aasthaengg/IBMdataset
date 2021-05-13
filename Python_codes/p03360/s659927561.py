# ABC 096: B – Maximum Sum
a = [int(s) for s in input().split()]
k = int(input())

a.sort()

print(sum(a) + a[2] * (2 ** k - 1))