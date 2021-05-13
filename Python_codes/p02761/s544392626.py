N, M = map(int, input().split())
SC = [list(map(int, input().split())) for _ in range(M)]
for i in range(1000):
    str_i = str(i)
    if len(str_i) == N and all(int(str_i[s-1])==c for s, c in SC):
        print(i)
        exit()
print(-1)
