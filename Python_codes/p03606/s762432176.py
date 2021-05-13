n = int(input())

tmp = [[int(j) for j in input().split()] for i in range(n)]

ans = sum([i[1]-i[0]+1 for i in tmp])
print(ans)