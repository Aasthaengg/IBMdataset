# omi

def main():
    n = int(input())

    print(0,flush=True)
    s = input()
    if s=="Vacant": return 0
    cap = 0
    if s=="Female": cap = 1

    lo = 0
    hi = n
    while True:
        mid = (hi+lo)//2
        print(mid, flush=True)
        s = input()

        if s=="Vacant": return 0
        gen = 0
        if s=="Female": gen = 1

        if (cap+mid)%2 == gen:
            lo = mid
        else:
            hi = mid

main()