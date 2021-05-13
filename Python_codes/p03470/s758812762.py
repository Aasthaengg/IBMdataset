def main():
    N = int(input())
    d = [int(input()) for _ in range(N)]
    d_set = set(d)
    ans = len(d_set)
    return ans

print(main())
