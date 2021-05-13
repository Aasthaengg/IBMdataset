from collections import Counter

def main():
    n = int(input())
    balls = [int(i) for i in input().split()]

    # v - value written on ball
    # b - ball index in [0, n)
    # ct - number of times a value occurs

    # hist[v] = ct
    hist = Counter(balls)
    diff_counts = set(hist.values())
    combos1 = { ct: 0 if ct == 1 else (ct-1) * (ct-2) // 2 for ct in
            diff_counts }
    combos = { ct: ct * (ct-1) // 2 for ct in diff_counts  }

    tot = sum(combos[hist[v2]] for v2 in hist.keys())

    for b in range(n):
        v = balls[b]
        ct = hist[v]
        print(tot - combos[ct] + combos1[ct])

main()
