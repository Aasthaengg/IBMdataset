A,B,C = map(int,input().split())

ans = 'NO'
for x in range(0,101):
    for y in range(0,101):
        if A * x == B * y + C:
            ans = 'YES'
print(ans)
