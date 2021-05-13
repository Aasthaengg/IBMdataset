loopCnt = int(input())
cards = list(map(int, input().split()))

alice = 0
bob = 0

cards.sort(reverse=True)

for i in range(loopCnt):
  if i == 0 or i%2 == 0:
    alice += cards[i]
  elif i%2 == 1:
    bob += cards[i]

print(alice-bob)