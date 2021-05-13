N = int(input())
a = [int(a) for a in input().split()]

sorted_a = sorted(a, reverse=True)

alice = sum(sorted_a[::2])
bob = sum(sorted_a[1::2])

print(alice-bob)