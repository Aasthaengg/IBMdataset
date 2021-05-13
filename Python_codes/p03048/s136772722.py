R,G,B,N = map(int,input().split())
ans = 0
for r in range(3001):
    for g in range(3001):
        b = (N-R*r-G*g)
        if b >= 0 and b%B == 0:
            ans += 1
print(ans)


