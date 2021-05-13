def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    dic = {}
    for i in range(n):
        if a[i] not in dic.keys():
            dic[a[i]] = 1
        else:
            dic[a[i]] += 1
    for i in range(m):
        b,c = map(int,input().split())
        if c not in dic.keys():
            dic[c] = b
        else:
            dic[c] += b
    cnt = 0
    ans = 0
    for k in sorted(dic.keys(),reverse=True):
        if cnt + dic[k] < n:
            ans += dic[k]*k
            cnt = cnt + dic[k]
        else:
            ans += k *(n-cnt)
            print(ans)
            return

if __name__ == "__main__":
    main()
