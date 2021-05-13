N = int(input())
a = list(map(int, input().split()))

alice = 0
bob = 0

for n in range(N):
    if len(a) == 0:
        break
    card = max(a)
    alice += card
    a.remove(card)
    if len(a) == 0:
        break
    card = max(a)
    bob += card
    a.remove(card)

print(alice - bob)