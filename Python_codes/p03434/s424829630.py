n = int(input())
a = sorted([int(X) for X in input().split()],reverse=True)
print(sum(a[::2])-sum(a[1::2]))