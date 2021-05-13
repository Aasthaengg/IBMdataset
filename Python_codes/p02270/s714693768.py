def main():
    n,k = map(int,input().split())
    a = []
    for _ in range(n):
        a.append(int(input()))

    def check(P):
        s = 0
        res = 1
        for b in a:
            if P<b:return False
            if P<s+b:
                s = b
                res+=1
            else :s+=b
        return k>=res

    l,r = 0,1000000007
    m = 0
    while l<r-1:
        m = (l+r)//2
        if check(m):r = m
        else       :l = m
    print(r)



if __name__ == '__main__':
    main()


