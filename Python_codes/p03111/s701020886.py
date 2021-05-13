from itertools import permutations

def main():
    n, a, b, c = map(int, input().split())
    l = [int(input()) for _ in range(n)]

    # full search
    ans = 10**9
    for perm in permutations(l):
        cost = -30
        for i in range(1, n-1):
            cost1 = cost + 10 * len(perm[:i]) + abs(a - sum(perm[:i]))
            for j in range(i+1, n):
                cost2 = cost1 + 10 * len(perm[i:j]) + abs(b - sum(perm[i:j]))
                for k in range(j+1, n+1):
                    cost3 = cost2 + 10 * len(perm[j:k]) + abs(c - sum(perm[j:k]))
                    if cost3 < ans:
                        ans = cost3

    print(ans)

main()