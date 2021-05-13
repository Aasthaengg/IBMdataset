# coding: utf-8

# https://atcoder.jp/contests/abc098/tasks/arc098_a


def main():
    N = int(input())
    S = input()
    
    ans = len([1 for s in S[1:] if s == "E"])
    now = ans
    for i in range(1, N):
        now += 1 if S[i-1] == "W" else 0
        now -= 1 if S[i] == "E" else 0

        if now < ans:
            ans = now
    
    return ans


print(main())
