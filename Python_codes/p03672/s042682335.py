#!/usr/local/bin/python3
# https://atcoder.jp/contests/abc066/tasks/abc066_b

S = list(input())[:-2]

def check(S):
    half = len(S) // 2
    if S[:half] == S[half:]:
        return True
    else:
        return False

while True:
    if check(S):
        print(len(S))
        break
    S = S[:-2]
