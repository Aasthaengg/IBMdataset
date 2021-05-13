N = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
alice = 0
bob = 0
for i, el in enumerate(a):
    if i % 2 == 0:
        alice += el
    else:
        bob += el
print(alice - bob)