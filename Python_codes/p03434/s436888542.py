n = int(input())
a = list(map(int, input().split()))
alice = []
bob = []

for i in range(n):
    if i % 2 == 0:
        alice.append(max(a))
        a.remove(max(a))
    else:
        bob.append(max(a))
        a.remove(max(a))

print(sum(alice)-sum(bob))