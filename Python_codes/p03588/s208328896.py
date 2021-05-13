n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
l.sort(key=lambda x: x[0])
print(l[-1][0] + l[-1][1])