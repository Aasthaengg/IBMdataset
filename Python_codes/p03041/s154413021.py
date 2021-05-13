#!/usr/bin/env python3
# N = int(input())
# S = input()
N, K = map(int, input().split())
S = [s for s in input()]
# A = list(map(int, input().split()))
S[K - 1] = S[K - 1].lower()
print("".join(S))