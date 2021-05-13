n,a,b = map(int, input().split())
ans = (b-a) * (n-2) + 1
print(ans if ans > 0 else 0)
