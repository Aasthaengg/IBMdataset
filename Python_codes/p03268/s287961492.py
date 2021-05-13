def main():
    n,k = tuple([int(t)for t in input().split()])

    if k%2==0:
        t = n//k#kの倍数
        s = n//(k//2)-t#k//2の倍数でkの倍数でない数
        ans = t**3+s**3
        print(ans)
    else:
        ans = (n//k)**3
        print(ans)

if __name__ == "__main__":
    main()