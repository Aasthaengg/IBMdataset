l, r = map(int, input().split())
n = r-l+1
ans1 = 0
ans2 = 0
min1 = 1000000000
min2 = 10000000000


for i in range(min(n, 2024)):
   # print(l+i)
    if (l+i) % 2019 == 0:
        print(0)
        break
else:
    ans = 10000000000
    for i in range(min(n, 2019)):
        for j in range(i+1, min(n, 2020)):
            # print(l+i, l+j)
            if ((l+i)*(l+j)) % 2019 < ans:
                ans = ((l+i)*(l+j)) % 2019
                # print(ans, l+i, l+j)
    print(ans)
