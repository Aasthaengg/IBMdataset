def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    n, h = map(int, input().split())
    aa, bb = [], []
    for i in range(n):
        a, b = map(int, input().split())
        aa.append(a)
        bb.append(b)
    bb.sort(reverse=True)
    maxa = max(aa)
    cnt = 0
    i=0
    
    while i < n and h > 0:
        if bb[i] > maxa:
            h -= bb[i]
            cnt+=1
        i+=1
    if h > 0:
        cnt += (h+maxa-1)//maxa
        
    print(cnt)
        
        
if __name__ == '__main__':
    main()