a, b, c, k = map(int, input().split())
ans = a - b
if abs(ans) > 1e18 :
    print("Unfair")
elif k % 2 == 0 :
    print(ans)
else :
    print(-ans)
