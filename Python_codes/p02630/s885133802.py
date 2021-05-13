from collections import Counter
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    cnt = Counter(A)


    ans = sum(A)
    for i in range(Q):
        B, C = map(int, input().split())
        ans += cnt[B] * (C - B)
        cnt[C] += cnt[B]
        cnt[B] = 0
        print(ans)

main()