def main():
    n=int(input())
    x=list(map(int,input().split()))
    sx = sorted(x)
    lx = len(x)//2
    m = sx[lx]
    _m = sx[lx-1] if 0 < m-1 else sx[0]
    for i in x:
        print(m if i<m else _m)

if __name__ == "__main__":
    main()