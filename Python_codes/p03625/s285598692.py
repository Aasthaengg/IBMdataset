#!/usr/bin/env python3

N = int(input())
# S = input()
# N, K = map(int, input().split())
A = list(map(int, input().split()))
from collections import Counter

def main():
    cnt = Counter(A).items()
    koho_2 = []
    koho_4 = []
    for k, v in cnt:
        if v >= 4:
            koho_4.append(k)
        if v >= 2:
            koho_2.append(k)
    ans = [0]
    koho_2 = sorted(koho_2)[::-1]
    koho_4 = sorted(koho_4)[::-1]
    if len(koho_2) >= 2:
        ans.append(koho_2[0] * koho_2[1])
    if len(koho_4) >= 1:
        ans.append(koho_4[0] ** 2)
    print(max(ans))

if __name__ == "__main__":
    main()
