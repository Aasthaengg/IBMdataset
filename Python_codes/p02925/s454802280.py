# E - League
import sys
from collections import deque
from typing import Deque, List

readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(readline())
    A: List[Deque[int]] = [deque()] + [
        deque(map(int, line.split())) for line in readlines()
    ]
    matched_games_cnt = 0
    next_games_opponent, last_games_day = [0] * (N + 1), [0] * (N + 1)
    queue = deque(list(range(1, N + 1)))
    while queue:
        player = queue.popleft()
        if not A[player]:  # The player has finished all games.
            continue
        opponent = A[player].popleft()

        # The opponent will have another game before playing against x.
        if next_games_opponent[opponent] != player:
            next_games_opponent[player] = opponent
            continue

        # The opponent's next game is against the player and vice versa.
        matched_games_cnt += 1
        last_games_day[player] = last_games_day[opponent] = (
            max(last_games_day[player], last_games_day[opponent]) + 1
        )
        # No next game is currently planned.
        next_games_opponent[player] = next_games_opponent[opponent] = 0
        queue.append(player), queue.append(opponent)

    print(max(last_games_day) if matched_games_cnt == N * (N - 1) // 2 else -1)


if __name__ == "__main__":
    main()
