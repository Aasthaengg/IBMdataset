N = int(input())
a = sorted(list(map(int,input().split())))

alice = []
bob = []
for i in range(N):
    if i % 2 == 0:
        alice.append(a[i])
    else:
        bob.append(a[i])

print(abs(sum(bob)-sum(alice)))