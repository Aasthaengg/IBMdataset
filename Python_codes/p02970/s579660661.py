n,d = map(int,input().split())

kansi = d * 2 + 1

ans = n // kansi

if n % kansi != 0:
    ans += 1

print(ans)