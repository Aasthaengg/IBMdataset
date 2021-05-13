N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

c = [i+j for i, j in AB]
c.sort(reverse = True)

ans = sum(c[::2]) - sum([j for i, j in AB])
print(ans)