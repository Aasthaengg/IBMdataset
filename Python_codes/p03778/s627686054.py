w, a, b = map(int, input().split())

if a < b:
    ans = b - (a+w)
    if ans <= 0:
        print(0)
    else:
        print(ans)
else:
    ans = a - (b+w)
    if ans <= 0:
        print(0)
    else:
        print(ans)
