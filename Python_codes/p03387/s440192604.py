a = list(map(int,input().split()))
a = sorted(a)
a,b,c = a[0],a[1],a[2]
ca = c-a
cb = c-b
if ca % 2 == 0 and cb % 2 == 0:
    print(ca //2 + cb //2)
elif ca % 2 == 1 and cb % 2 == 1:
    print(((ca-1) // 2) + ((cb-1) // 2) + 1)
elif ca % 2 == 1 and cb % 2 == 0:
    print((cb // 2) + 1 + ((ca+1) // 2))
elif cb % 2 == 1 and ca % 2 == 0:
    print((ca // 2) + 1 + ((cb+1) // 2))