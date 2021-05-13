def main():
    n = int(input())
    a = sorted(list(map(int,input().split())))
    t = a[-1]
    s = t/2
    z = a[0]
    for i in range(1,n-1):
        if abs(a[i]-s)<abs(z-s):
            z = a[i]
    print(t,z)

if __name__ == "__main__":
    main()
