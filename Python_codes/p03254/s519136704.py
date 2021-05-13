n, x = map(int, input().split())
a = sorted(map(int, input().split()))
rest = x
ans = 0
for i in range(n) :
    if rest > a[i] :
        if i != n-1 :
            rest -= a[i]
            ans += 1
        else :
            print(ans)
            break
    elif rest == a[i] :
        ans += 1
        print(ans)
        break
    else :
        print(ans)
        break
else :
    print(ans)
