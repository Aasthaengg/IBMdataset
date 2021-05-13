def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    h = {}
    for i in range(m):
        b,c = map(int,input().split())
        if c not in h.keys():
            h[c] = b
        else:
            h[c]+=b
    for i in range(n):
        if a[i] not in h.keys():
            h[a[i]]=1
        else:
            h[a[i]]+=1
    ans = 0
    for k in sorted(h.keys(),reverse=True):
        if n<h[k]:
            ans += n*k
            break
        ans += h[k]*k
        n = n-h[k]
    print(ans)


if __name__ == "__main__":
    main()
