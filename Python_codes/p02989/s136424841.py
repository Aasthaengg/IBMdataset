N = int(input())
d = list(map(int,input().split()))
d.sort()

ans = d[len(d) // 2] - d[len(d) // 2 -1]
print(ans)