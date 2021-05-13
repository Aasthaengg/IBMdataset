def main():
    n,m=map(int,input().split())
    s=input()
    masu = n
    res = []
    while masu>m:
        tm = m
        while s[masu - tm]=="1":
            tm -= 1
            if tm == 0:
                return -1
        res.append(tm)
        masu -= tm
    res.append(masu)
    res.reverse()
    return " ".join(map(str,res))


print(main())