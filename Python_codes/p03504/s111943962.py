# ABC080D - Recording
def main():
    N, C, *STC = map(int, open(0).read().split())
    recorders = [[0] * (10 ** 5 + 1) for _ in range(C + 1)]
    for s, t, c in zip(*[iter(STC)] * 3):
        recorders[c][s - 1 : t] = [1] * (t - s + 1)
    ans = max(sum(sliced) for sliced in zip(*recorders))
    print(ans)


if __name__ == "__main__":
    main()