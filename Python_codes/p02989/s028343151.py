n = int(input())
d = list(map(int, input().split()))
sort_d = sorted(d)
ans = sort_d[n//2] - sort_d[n//2 - 1]
print(ans)