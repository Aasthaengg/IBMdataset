n = int(input())
a = list(map(int, input().split()))
a.sort()
if n%2 == 0:
    alice = sum(a[1::2])
    bob = sum(a[::2])
else:
    alice = sum(a[::2])
    bob = sum(a[1::2])
print(alice-bob)