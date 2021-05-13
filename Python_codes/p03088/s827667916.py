import functools
import itertools
import collections

l = list("ACGT")

@functools.lru_cache(maxsize=None)
def f(d, sl, e):
    if e == d:
        return 1
    else:
        cnt = 0
        for v in l:
            tsl = collections.deque(sl)
            if len(sl) == 4:
                tsl.popleft()
            tsl.append(v)
            ts = "".join(tsl)
            if len(ts) >= 3 and (ts[-3:] == "AGC" or ts[-3:] == "GAC" or ts[-3:] == "ACG"):
                continue
            if len(ts) >= 4 and ts[0] == "A" and ts[2:] == "GC":
                continue
            if len(ts) >= 4 and ts[:2] == "AG" and ts[3] == "C":
                continue
            cnt += f(d + 1, ts, e)
        return cnt


def slove():
    import sys
    input = sys.stdin.readline
    e = int(input().rstrip('\n'))
    sl = []
    print(f(0, "".join(sl), e) % (10 ** 9 + 7))


if __name__ == '__main__':
    slove()
