n = int(input())
a = list(map(int, input().split()))

alice = 0
bob = 0

a.sort()
a.reverse()

for i in a[::2]:
    alice += i

for j in a[1::2]:
    bob += j

print(alice-bob)