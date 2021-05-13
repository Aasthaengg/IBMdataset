def main():
    from collections import Counter
    N = int(input())
    S_count = Counter(input())
    P = 10**9+7
    ans = 1
    for v in S_count.values():
        ans *= v+1
        ans %= P
    print(ans-1)



main()