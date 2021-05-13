n, h, w = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(n)]
print(len(list(filter(lambda x: x[0] >= h and x[1] >= w, AB))))
