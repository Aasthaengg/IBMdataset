n = int(input())
cards = sorted(list(map(int, input().split())), reverse=True)
alice = []
bob = []
for i in range(0, n, 2):
    alice.append(cards[i])
    try:
        bob.append(cards[i+1])
    except:
        break
print(sum(alice) - sum(bob))