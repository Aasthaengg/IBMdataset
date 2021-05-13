n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]
info = sorted(info, reverse=True)
print(info[0][0] + info[0][1])