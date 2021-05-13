n,a,b = map(int,input().split())
ans = [min(a,b), max(0,(a+b)-n)]
print(*ans, sep=' ')
