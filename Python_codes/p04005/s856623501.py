a, b, c = map(int, input().split())

if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    print(0)
else:
    li_wk = sorted([a, b, c], reverse=True)
    print(li_wk[1] * li_wk[2])
