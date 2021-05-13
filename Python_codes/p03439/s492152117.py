N = int(input())
# とりあえず先頭の性別を取得する
print(0)
begin = input()

l, r = 0, N
while r - l > 1:
    mid = (l+r)//2
    print(mid)
    sex = input()
    if sex == "Vacant":
        l = mid
        break
    elif mid % 2 == 0:
        if sex != begin:
            r = mid
        else:
            l = mid
    else:
        if sex != begin:
            l = mid
        else:
            r = mid

print(l)
