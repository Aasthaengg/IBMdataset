import sys

N = int(input())

print (0)
l = 0
ln = input()

if ln == "Vacant":
    sys.exit()

print (N-1)
r = N-1
rn = input()

if rn == "Vacant":
    sys.exit()


while True:

    mid = (l + r) // 2
    print (mid)
    mn = input()

    if mn == "Vacant":
        sys.exit()

    if (mid - l) % 2 == 0:

        if ln == mn:
            l = mid
            ln = mn

        else:
            r = mid
            rn = mn

    else:

        if ln == mn:
            r = mid
            rn = mn

        else:
            l = mid
            ln = mn
