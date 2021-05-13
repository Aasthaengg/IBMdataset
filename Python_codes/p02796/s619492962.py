from collections import deque
from operator import itemgetter
def main():
    n = int(input())
    robots = []
    for _ in range(n):
        x, l = map(int, input().split())
        lside = x - l
        rside = x + l
        robots.append((lside, rside))
    # ロボットの腕の右端を基準にして昇順ソート。
    robots = sorted(robots, key=itemgetter(1))
    robots = deque(robots)
    a_robot = robots.popleft()
    cnt = n
    while robots:
        robot_next = robots.popleft()
        if a_robot[1] > robot_next[0]:
            cnt -= 1
        else:
            a_robot = robot_next
            continue
    print(cnt)

if __name__ == '__main__':
    main()
