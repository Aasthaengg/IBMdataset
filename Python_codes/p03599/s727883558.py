A,B,C,D,E,F = map(int, open(0).read().split())
ans = [0] * 3
for a in range(F//(100*A)+1):
    for b in range((F-(100*A)*a)//(100*B)+1):
        if a == 0 and b == 0:
            continue
        else:
            m = min(((A*a)+(B*b))*E,F-(100*((A*a)+(B*b))))
            sugar = 0
            for c in range(m//C+1):
                sugar = max(sugar,m-(m-C*c)%D)
                if sugar == m:
                    break
            temp = sugar / (100*((A*a)+(B*b))+sugar)
            if temp > ans[0]:
                ans[0] = temp
                ans[1] = 100 * ((A*a)+(B*b)) + sugar
                ans[2] = sugar
if ans[1] == 0:
    ans[1] = 100 * A
print(ans[1],ans[2])