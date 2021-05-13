a,b,c,d,e,f = list(map(int, input().split()))
maxn = -1
ans = ()
for at in range(0,31):
    for bt in range(0,31-at):
        water = (at * a + bt * b) * 100
        if water > f:
            continue

        # 溶け残らないように砂糖を選ぶ
        maxsugar = water * e // 100
        for ct in range(0, maxsugar//c + 1):
            for dt in range(0, (maxsugar-ct*c)//d + 1):
                sugar = ct * c + dt * d

                if 0 < sugar + water <= f and sugar <= (at * a + bt * b) * e:
                    # 水１００に対して溶けている砂糖の量
                    n = 100 * sugar / water
                    if n == e:
                        print(water + sugar, sugar)
                        exit()
                    if n > maxn:
                        ans = water + sugar, sugar
                        maxn = n
print(*ans)