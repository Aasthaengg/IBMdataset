r, l = map(int, input().split())
ans = 2018
for i in range(r,l):
    for j in range(r+1,l+1):
        if ans > (i*j) % 2019:
            ans = (i*j) % 2019
            if ans == 0:
                break

    if ans == 0:
        break

print(ans)
