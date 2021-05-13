n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort(reverse=True)
print(sum(ab[0]))