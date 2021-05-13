k = int(input())
a = list(map(int, input().split()))
a.reverse()

mn,mx = 2,2
for g in a:
    mn = g * (((mn - 1) // g) + 1)
    mx = g * (mx//g) + g - 1

    if mn > mx:
        print(-1)
        exit()

print(mn,mx)