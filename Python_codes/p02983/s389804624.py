L, R = map(int, input().split())
ans = 2018
for i in range(L, R):
    for j in range(L+1, R+1):
        if ans > (i*j) % 2019:
            ans = (i*j) % 2019
            if ans==0:
                break
    if ans == 0:
        break
print(ans)
