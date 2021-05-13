def main():
    n,k = map(int,input().split())
    s = input()

    res = []
    buf = '1' # start:1 kara NG->s[0]
    cnt = 0
    for i in range(n):
        if s[i] == buf:
            cnt += 1
        else:
            res.append(cnt)
            buf = s[i]
            cnt = 1
    if cnt != 0:
        res.append(cnt)

    if len(res)%2 == 0:
        res.append(0) # end:1 no kosu

    #from itertools import accumulate
    #rui = list(accumulate(res))
    rui = [0]*(len(res)+1)
    for i in range(len(rui)-1):
        rui[i+1] = rui[i] + res[i]

    ans = 0
    for i in range(0,len(res),2): # 1 only
        left = i
        right = min(i+2*k+1, len(res))
        tmp = rui[right] - rui[left]
        ans = max(tmp,ans)
    print(ans)

if __name__ == '__main__':
    main()
