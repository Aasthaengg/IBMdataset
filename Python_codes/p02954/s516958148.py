import bisect

def main():
    S = list(input())
    r_idx = [i for i, s in enumerate(S) if s == 'R']
    l_idx = [i for i, s in enumerate(S) if s == 'L']
    ans = [0] * len(S)
    for i, s in enumerate(S):
        if s == 'R':
            idx = bisect.bisect_left(l_idx, i)
            if (l_idx[idx] - i) % 2 == 0:
                ans[l_idx[idx]] += 1
            else:
                ans[l_idx[idx] - 1] += 1
        else:
            idx = bisect.bisect_left(r_idx, i) - 1
            if (i - r_idx[idx]) % 2 == 0:
                ans[r_idx[idx]] += 1
            else:
                ans[r_idx[idx] + 1] += 1
    print(" ".join([str(v) for v in ans]))


if __name__ == '__main__':
    main()
