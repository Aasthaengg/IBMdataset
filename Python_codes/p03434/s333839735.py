n = int(input())
a = [int(x) for x in input().split()]
a.sort(reverse=True)

alice = a[::2]
bob = a[1::2]
print(sum(alice) - sum(bob))