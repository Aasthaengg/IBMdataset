def main():
    n = int(input())
    a = list(map(int,input().split()))
    d = {}
    for i in range(n):
        if d.get(a[i]) == None:
            d[a[i]] = 1
        else:
            d[a[i]] += 1
    ans = 0
    for k in d.keys():
        ans += d[k] * (d[k]-1) //2
    for i in range(n):
        print(ans - ((d[a[i]]*(d[a[i]]-1))//2 - (d[a[i]]-1) * (d[a[i]]-2)//2))

if __name__ == "__main__":
    main()
