#!/usr/bin/env python3
def main():
    N, M = map(int, input().split())
    k, s = [], []
    for _ in range(M):
        lst = [int(x) - 1 for x in input().split()]
        k.append(lst.pop(0) + 1)
        s.append(set(lst))
    p = [int(x) for x in input().split()]

    ans = 0
    for bit in range(1 << N):
        now_on_switch = []
        for i in range(N):
            if bit & (1 << i):
                now_on_switch.append(i)
        lights = 0
        for i in range(M):
            cnt = 0
            for j in now_on_switch:
                cnt += 1 if j in s[i] else 0
            lights += 1 if cnt % 2 == p[i] else 0
        ans += 1 if lights == M else 0
    print(ans)


if __name__ == '__main__':
    main()
