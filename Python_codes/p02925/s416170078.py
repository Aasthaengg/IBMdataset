# E - League
import sys
from collections import deque
from typing import Deque, List

readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(readline())
    schedules: List[Deque[int]] = [deque()] + [
        deque(map(int, line.split())) for line in readlines()
    ]
    matched_games_cnt = 0
    next_opponents, last_games_days = [0] * (N + 1), [0] * (N + 1)
    queue = deque(range(1, N + 1))
    while queue:
        player = queue.popleft()
        if not schedules[player]:  # The player has finished all games.
            continue
        opponent = schedules[player].popleft()

        # The opponent will have another game before playing against x.
        if next_opponents[opponent] != player:
            next_opponents[player] = opponent
            continue

        # The opponent's next game is against the player and vice versa.
        matched_games_cnt += 1
        last_games_days[player] = last_games_days[opponent] = (
            max(last_games_days[player], last_games_days[opponent]) + 1
        )
        # No next game is currently planned.
        next_opponents[player] = next_opponents[opponent] = 0
        queue.append(player), queue.append(opponent)

    print(max(last_games_days) if matched_games_cnt == N * (N - 1) // 2 else -1)


if __name__ == "__main__":
    main()
