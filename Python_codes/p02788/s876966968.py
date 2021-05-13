import sys
from collections import deque

read = sys.stdin.buffer.read


def main():
    N, D, A, *XH = map(int, read().split())
    monster = [0] * N
    for i, (x, h) in enumerate(zip(*[iter(XH)] * 2)):
        monster[i] = (x, (h + A - 1) // A)

    monster.sort()

    dq = deque([])
    damage = 0
    ans = 0

    for x, h in monster:
        while dq and dq[0][0] < x:
            damage -= dq.popleft()[1]

        if h > damage:
            dq.append((x + 2 * D, h - damage))
            ans += h - damage
            damage += h - damage

    print(ans)
    return


if __name__ == '__main__':
    main()
