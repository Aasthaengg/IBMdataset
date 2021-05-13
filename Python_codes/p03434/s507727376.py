n = int(input())
a = [int(s) for s in input().split()]

a.sort()
alice = 0
bob = 0
for i in range(n):
    if i % 2 == 0:
        alice += a[n-1-i]
    elif i % 2 == 1:
        bob += a[n-1-i]

print(alice - bob)
