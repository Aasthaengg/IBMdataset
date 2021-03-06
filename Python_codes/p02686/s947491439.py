def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n = int(input())
    lx = []
    rx = []
    for i in range(n):
        a = 0
        cnt = 0
        for j in input():
            if j == '(':
                cnt += 1
            else:
                cnt -= 1
            a = min(a, cnt)
        
        if cnt >= 0:
            lx.append((a, cnt))
        else:
            rx.append((a, cnt))
    lx.sort(key= lambda x: -x[0]) # -aの昇順
    rx.sort(key= lambda x: x[0]-x[1]) # -bの昇順(bの降順)
    total = 0
    check = True
    for x,cnt in (lx+rx):
        if total + x < 0:
            check = False
            break
        total += cnt
    if total == 0 and check:
        print('Yes')
    else:
        print("No")
    




if __name__ == '__main__':
    main()