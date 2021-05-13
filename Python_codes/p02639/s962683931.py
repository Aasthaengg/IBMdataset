x = list(map(int, input().split()))
ans = 0
if x[0] == 0:
    ans = x[1] - 1
else:
    for i in range(1, len(x)):
        if x[i] == 0:
            ans = x[i-1] + 1

print(ans)