N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
AB = sorted(AB, key=lambda x:sum(x), reverse=True)

print(sum(map(lambda x: x[0], AB[::2])) - sum(map(lambda x: x[1], AB[1::2])))
