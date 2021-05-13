n = int(input())
ans = 0
if n < 105:
    print(0)
else:
    for i in range(1,n+1,2):
        count = 0
        for l in range(1, i+1, 2):
            if i % l == 0:
                count += 1
        if count == 8:
            ans += 1
    print(ans)