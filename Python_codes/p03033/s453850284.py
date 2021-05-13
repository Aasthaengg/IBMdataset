def main():
    n,q = map(int, input().split())
    tl = []
    que = []
    d = dict()
    for _ in range(n):
        s,t,x = map(int, input().split())
        tl.append((s-x,1,x))
        tl.append((t-x,0,x))
    for _ in range(q):
        t = int(input())
        tl.append((t,2))
    tl.sort()
    wor = set()
    wcur = 0
    cur = -1
    flg = 0
    for x in tl:
        if x[1] == 1:
            wcur += 1
            wor.add(x[2])
            if cur < 0 or x[2] < cur:
                cur = x[2]
                flg = 0
        elif x[1] == 0:
            wcur -= 1 
            wor.remove(x[2])
            if x[2] == cur:
                flg = 1
            if not wcur:
                cur = -1
                flg = 0
        else:
            if flg:
                cur = min(wor)
                flg = 0
            print(cur)
    
if __name__ == "__main__":
    main()
