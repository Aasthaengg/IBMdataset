N = int(input())
a = sorted(map(int, input().split()), reverse=True)

alice, bob = 0, 0

for i in range(N):
    if i % 2 == 0:
        alice += a[i]
    else:
        bob += a[i]

print(alice - bob)
