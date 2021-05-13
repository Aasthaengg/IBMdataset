import itertools
from collections import defaultdict

def main():
    name_freq = defaultdict(int)
    N = int(input())
    for _ in range(N):
        name_freq[input()[0]] += 1

    ans = 0
    for comb in itertools.combinations(['M', 'A', 'R', 'C', 'H'], 3):
        ans += name_freq[comb[0]] * name_freq[comb[1]] * name_freq[comb[2]]
    print(ans)


if __name__ == '__main__':
    main()
