a, b = map(int, input().split())
ans = "Possible"

if a % 3 == 0:
    pass
elif b % 3 == 0:
    pass
elif (a + b) % 3 == 0:
    pass
else:
    ans = "Impossible"

print(ans)