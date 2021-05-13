N = int(input())
a = list(map(int,input().split()))

a.sort(reverse=True)
alice = []
bob = []


for i in range(N):
    if i % 2 == 0:
        alice.append(a[i])
    else:
        bob.append(a[i])

print(sum(alice) - sum(bob))