n, k = map(int, input().split())
x = tuple(map(int, input().split()))

md = 20**8 + 1
for l in range(n-k+1):
    r = l+k-1
    md = min(md, abs(x[l]) + abs(x[l] - x[r]))
    md = min(md, abs(x[r]) + abs(x[l] - x[r]))
print(md)
