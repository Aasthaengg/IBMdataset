from collections import deque
card = {'a' : deque(input()), 'b' : deque(input()), 'c' : deque(input())}

player = card['a'].popleft()
while card[player]:
    player = card[player].popleft()

print(player.upper())