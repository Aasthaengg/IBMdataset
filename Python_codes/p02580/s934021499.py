import sys
import itertools


def resolve(in_):
    H, W, M = map(int, next(in_).split())
    targets = tuple(tuple(map(int, line.split())) for line in in_)
    
    target_h = {}
    target_w = {}
    target_hw = set()
    for h, w in targets:
        target_h[h] = target_h.setdefault(h, 0) + 1
        target_w[w] = target_w.setdefault(w, 0) + 1
        target_hw.add((h, w))

    max_h = max(target_h.values())
    max_w = max(target_w.values())

    h_set = {h for h, v in target_h.items() if max_h == v}
    w_set = {w for w, v in target_w.items() if max_w == v}

    ans = max_h + max_w - 1
    for hw in itertools.product(h_set, w_set):
        if hw not in target_hw:
            ans += 1
            break
    
    return ans


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
