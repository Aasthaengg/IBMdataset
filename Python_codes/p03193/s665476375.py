N, H, W = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
print(len(list(filter(lambda ab: ab[0] >= H and ab[1] >= W, AB))))
