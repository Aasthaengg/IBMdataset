N = int(input())
d = list(map(int, input().split()))

sortd = sorted(d)
ans = sortd[int(N/2)] - sortd[int(N/2-1)]
print(ans)
