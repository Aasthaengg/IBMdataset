#!/usr/bin/env python3

N = int(input())
# S = input()
# N, K = map(int, input().split())
P = list(map(int, input().split()))

def main():
    ans = 0
    for i, p in enumerate(P, 1):
        if i == p:
            ans += 1
            if i != N:
                P[i] = p
    print(ans)

if __name__ == "__main__":
    main()
