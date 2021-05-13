def main():
    n,a,b = map(int,input().split())
    x = [int(x_) for x_ in input().split()]
    now = x[0]
    ans = 0
    for i in range(1,n):
        if (x[i]-now)*a<=b:
            ans += (x[i]-now)*a
        else:
            ans += b
        now = x[i]
    print(ans)
if __name__ == "__main__":
    main()