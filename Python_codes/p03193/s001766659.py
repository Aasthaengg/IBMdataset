N, H, W = map(int, input().split())
ok = lambda ab: ab[0]>=H and ab[1]>=W
print(sum(ok(tuple(map(int, input().split()))) for _ in range(N)))