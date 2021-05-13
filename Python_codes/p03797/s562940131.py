s, c = map(int, input().split())

ans = 0

if s == 1 and c == 1:
    print(ans)
    exit()

if 2*s >= c:
    ans = c//2
else:
    ans = s+ ( c - 2*s )//4

print(ans)                                                          