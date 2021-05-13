n = int(input())
cnt, ans = 0, 0
if n == 105:
    print(1)
elif n <= 104:
    print(0)
else:
    for x in range(107,n+1,2):
        cnt = 0
        for y in range(1,x+1):
            if x % y == 0:
                cnt += 1
        if cnt == 8:
            ans += 1
    print(ans+1)