from collections import OrderedDict

cards = OrderedDict()
cards['S'] = set()
cards['H'] = set()
cards['C'] = set()
cards['D'] = set()

n = int(input())
for _ in range(n):
    suit, num = input().split()
    num = int(num)
    cards[suit].add(num)

for suit, nums in cards.items():
    for num in range(1,14):
        if num not in nums:
            print(suit, num)