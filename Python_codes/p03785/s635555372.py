import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, C, K, *T = map(int, read().split())
T.sort()

def main(N, C, K, T):
    INF = K + 100
    time = -INF
    people = 0
    bus = 0
    for t in T:
        if t > time + K:
            time = t
            people = 1
            bus += 1
            continue
        if people < C:
            # 乗れる
            people += 1
        else:
            # 乗れない
            time = t
            people = 1
            bus += 1
    return bus

print(main(N, C, K, T))