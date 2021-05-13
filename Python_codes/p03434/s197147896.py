N = int(input())
A = list(map(int, input().split()))
alice = 0
bob = 0
A.sort(reverse=True)
for i in range(N):
    if i%2 == 0:
        alice += A.pop(0)
    else:
        bob += A.pop(0)
print(alice-bob)