N = int(input())
AB = [list(map(int, input().split())) for i in range(N)]
v = max(AB)
print(v[0]+v[1])