N = int(input())
d = map(int, input().split())
d = sorted(d, reverse = False)

ans = d[N//2] - d[N//2-1]
print (ans)