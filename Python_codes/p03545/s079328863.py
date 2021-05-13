a = list(map(int, list(input())))

for i in [True, False]:
    for j in [True, False]:
        for k in [True, False]:
            if i:
                ans = a[0] + a[1]
            else:
                ans = a[0] - a[1]
            if j:
                ans += a[2]
            else:
                ans -= a[2]
            if k:
                ans += a[3]
            else:
                ans -= a[3]
            if ans == 7:
                ans = str(a[0])
                if i:
                    ans += '+'
                else:
                    ans += '-'
                ans += str(a[1])
                if j:
                    ans += '+'
                else:
                    ans += '-'
                ans += str(a[2])
                if k:
                    ans += '+'
                else:
                    ans += '-'
                ans += str(a[3]) + '=7'
                print(ans)
                exit()