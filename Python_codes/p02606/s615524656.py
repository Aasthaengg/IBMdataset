l,r,d = map(int, input().split())
k1 = (l - 1) // d
k2 = r // d
ans = k2 - k1
print(ans)