n = int(input())
print(0)
st = input()
if st == "Vacant":
    exit()
print(n - 1)
en = input()
if en == "Vacant":
    exit()
l = 1
r = n - 1

while True:
    mid = (l + r) // 2
    print(mid)
    ask = input()
    if ask == "Vacant":
        exit()
    if (mid - l) & 1:
        if st == ask:
            l = mid + 1
            st = ask
        else:
            r = mid
            en = ask
    else:
        if st == ask:
            r = mid
            en = ask
        else:
            l = mid + 1
            st = ask
