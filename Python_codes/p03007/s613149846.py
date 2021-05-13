import sys

def bigsmall(x,y):
    return (x,y) if x>y else (y,x)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    if len(a) == 2:
        b,s = bigsmall(a[0],a[1])
        print(b-s)
        print(b,s)
        sys.exit()

    ops = []
    curr = 0
    b,s = bigsmall(a[0],a[-1])
    if a[1] <= 0:
        ops.append((b,s))
        curr = b - s
    else:
        ops.append((s,b))
        curr = s - b

    del a[-1]
    a.append(-1) # to set answer > 0

    for i in range(1, len(a)-1):
        b,s = bigsmall(curr,a[i])

        if a[i+1] <= 0:
            ops.append((b,s))
            curr = b - s
        else:
            ops.append((s,b))
            curr = s - b

    print(curr)
    for x,y in ops:
        print(x,y)

if __name__=='__main__':
    main()