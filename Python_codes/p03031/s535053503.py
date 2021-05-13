def main():
    n, m = list(map(int, input().split(" ")))
    k_list = []
    s_list = []
    for _ in range(m):
        s = []
        for i, one in enumerate(input().split(" ")):
            if i==0:
                k = int(one)
            else:
                s.append(int(one))
        k_list.append(k)
        s_list.append(s)
    p = list(map(int, input().split(" ")))

    cnt = 0
    for x in range(2**n):
        f = 0
        onoff_list = [1 if bin(x)[2:].zfill(n)[i]=="1" else 0 for i in range(n)]
        for mi in range(m):
            s = s_list[mi]
            on_num = sum([onoff_list[si-1] for si in s])
            if on_num%2==p[mi]:
                f+=1
            else:
                break
        if f==m:
            cnt+=1
    print(cnt)

if __name__=="__main__":
    main()
