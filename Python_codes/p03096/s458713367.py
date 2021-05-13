from collections import defaultdict

N = int(input())
stones = []
last = None
n_stone = 0
for i in range(N):
    stone = int(input())
    if stone != last:
        stones.append(stone)
        last = stone

count = defaultdict(int)
seq = 1
for i, c in enumerate(stones):
      prev = count[c]
      count[c] = prev + seq
      seq += prev

print(seq % (10**9 + 7))