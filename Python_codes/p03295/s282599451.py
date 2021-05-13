from operator import itemgetter
from collections import deque
def main():
    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(m)]

    ab = sorted(ab, key=itemgetter(1))
    ab = deque(ab)

    cnt = 1
    me = ab.popleft()
    while ab:
        me_n = ab.popleft()
        if me_n[0] < me[1]:
            continue
        else:
            cnt += 1
            me = me_n
    print(cnt)


if __name__ == '__main__':
    main()