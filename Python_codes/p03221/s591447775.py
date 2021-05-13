from collections import defaultdict
import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    PY = [tuple([i] + list(map(int, input().split()))) for i in range(M)]
    result = []
    p_city = defaultdict(int)
    for py in sorted(PY, key = lambda x: x[2]):
        p_city[py[1]] += 1
        code = str(py[1]).zfill(6) + str(p_city[py[1]]).zfill(6)
        result.append((py[0], code))
    print("\n".join([r[1] for r in sorted(result, key = lambda x: x[0])]))


if __name__ == '__main__':
    main()
