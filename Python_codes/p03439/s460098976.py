N = int(input())


def isOK(mid, x):
    print(str(mid), flush=True)
    s = input().strip()
    if s == "Vacant":
        exit()
    if (x and s == "Male") or (not x and s == "Female"):
        return True
    else:
        return False


ok = 0
ng = N

print("0", flush=True)
S = input().strip()
if S == "Vacant":
    exit()

if S == "Male":
    kijun = True
else:
    kijun = False

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if mid % 2 == 0:
        if isOK(mid, kijun):
            ok = mid
        else:
            ng = mid
    else:
        if isOK(mid, not kijun):
            ok = mid
        else:
            ng = mid

