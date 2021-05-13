def main():
    n = int(input())
    a = sorted(list(map(int,input().split())))
    ls = [0 for i in range(a[-1])]
    for i in range(n):
        if ls[a[i]-1] == -1:
            continue
        elif ls[a[i]-1]==1:
            ls[a[i]-1] = -1
        else:
            ls[a[i]-1] = 1
            for j in range(2,a[-1]//a[i]+1):
                ls[a[i]*j-1] = -1
    ans = 0
    for i in range(len(ls)):
        if ls[i]==1:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
