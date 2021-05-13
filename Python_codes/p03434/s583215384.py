N =int(input())
l = [int(i) for i in input().split()]
l.sort(reverse=True)
alice = l[0::2]
bob = l[1::2]
print(sum(alice) - sum(bob))