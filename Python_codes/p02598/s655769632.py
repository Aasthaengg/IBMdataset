def possible(x):
    global k
    cnt = 0
    for i in a:
        if i % x == 0:
            cnt += i // x - 1
        else:
            cnt += i // x

    if cnt <= k:
        return True
    return False

n, k = map(int, input().split())

a = list(map(int, input().split()))

mini = 1
maxi = max(a)

while mini <= maxi:
    mid = (mini + maxi) // 2
    res = possible(mid)
    if res:
        maxi = mid
    else:
        mini = mid
    # print(mini, mid, maxi)

    if mini+1 >= maxi:
        if maxi < mini:
            mini, maxi = maxi, mini
        if possible(mini):
            ans = mini
        else:
            ans = maxi
        break

print(ans)
# print(possible(4))

