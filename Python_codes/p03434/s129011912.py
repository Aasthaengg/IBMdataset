from collections import deque

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
a = deque(a)
alice = []
bob = []
for i in range(len(a)):
    if i % 2 == 0:
        alice.append(a.popleft())
    else:
        bob.append(a.popleft())
print(sum(alice) - sum(bob))