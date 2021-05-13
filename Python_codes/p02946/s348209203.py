p = list(map(int, input().split()))
ans  = list(range(p[1]-p[0]+1, p[1]+p[0]))
print(*ans)