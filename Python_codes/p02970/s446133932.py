n, d = map(int, input().split())

d = d*2 + 1

ans = n//d

if n%d == 0:
    print(ans)
else:
    print(ans + 1)