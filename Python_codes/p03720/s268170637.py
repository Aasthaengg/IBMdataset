n, m = map(int,input().split())
R = list(list(map(int, input().split())) for _ in range(m))
for i in range(1, n+1):
    print(sum(R, []).count(i))