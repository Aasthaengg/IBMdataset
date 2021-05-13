n = int(input())
arr = sorted(list(map(int,input().split())))
ans = 0
ok1 = False
ok2 = False
for i in arr:
    if i > 0:
        ok1 = True
    else:
        ok2 = True
if ok1 and ok2:
    for i in arr:
        ans += i if i > 0 else -i
    print(ans)
    ope1 = arr.pop()
    ope2 = arr.pop(0)
    for a in arr:
        if a > 0:
            print(ope2,a)
            ope2 -= a
        else:
            print(ope1,a)
            ope1 -= a
    print(ope1,ope2)
else:
    if ok1:
        ans = sum(arr) - 2*arr[0]
        print(ans)
        ope1 = arr.pop(0)
        for i in range(n-2):
            print(ope1,arr[i])
            ope1 -= arr[i]
        print(arr[-1],ope1)
    else:
        ans = -sum(arr) + 2*arr[-1]
        print(ans)
        ope2 = arr.pop(-1)
        for i in range(n-1):
            print(ope2,arr[i])
            ope2 -= arr[i]
