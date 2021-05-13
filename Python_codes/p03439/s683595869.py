import sys
def main():
    n = int(input())
    print("0")
    sys.stdout.flush()
    x = input().rstrip()
    if x == "Vacant":
        sys.exit()
    print(n//2)
    sys.stdout.flush()
    y = input().rstrip()
    if y == "Vacant":
        sys.exit()
    l, r= 0, 0
    z = ""
    if x == y:
        if n//2%2 == 1:
            l = 0
            r = n//2
            z = x
        else:
            l = n//2
            r = n
            z = y
    else:
        if n//2%2 == 1:
            l = n//2
            r = n
            z = y
        else:
            l = 0
            r = n//2
            z = x
    while True:
        p = (l+r)//2
        print(p)
        sys.stdout.flush()
        w = input().rstrip()
        if w == "Vacant":
            sys.exit()
        if z == w:
            if l%2 == p%2:
                l = p
            else:
                r = p
        else:
            if l%2 == p%2:
                r = p
            else:
                l = p
                z = w

if __name__ == "__main__":
    main()
