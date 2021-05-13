l, r = map(int, input().split())

rem_l = l%2019
rem_r = r%2019

ans = -1

if r - l >= 2019:
    ans = 0

elif rem_l >= rem_r:
    ans = 0

else:
    ans = float('INF')
    for i in range(l, r+1):
        for j in range(i+1, r+1):
            temp = (i * j) % 2019
            if temp < ans:
                ans = temp

print(ans)
