a, b, c = map(int, input().split())
if (a+b+c)%2 :
    if a%2 and b%2 and c%2 :
        total = a + b + c
        mx = max(a,b,c)
        diff = 3*mx - total
        print(diff//2)
    else :
        if not a%2 :
            a += 1
        if not b%2 :
            b += 1
        if not c%2 :
            c += 1
        total = a + b + c
        mx = max(a,b,c)
        diff = 3*mx -total
        ans = 1 + diff//2
        print(ans)
else :
    if not (a%2 or b%2 or c%2) :
        total = a + b + c
        mx = max(a,b,c)
        diff = 3*mx -total
        print(diff//2)
    else :
        if a%2 :
            a += 1
        if b%2 :
            b += 1
        if c%2 :
            c += 1
        total = a + b + c
        mx = max(a,b,c)
        diff = 3*mx - total
        ans = 1 + diff//2
        print(ans)
