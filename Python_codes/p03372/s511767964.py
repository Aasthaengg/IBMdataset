import sys
input = sys.stdin.buffer.readline

def main():
    N,C = map(int,input().split())
    susi = [tuple(map(int,input().split())) for _ in range(N)]
    csusi = list(reversed(susi))
    
    cal,ccal = 0,0
    now,cnow = 0,0
    eat,ceat = [(0,0)],[(0,0)]
    for i,j in zip(susi,csusi):
        x,v = i
        cal += v
        if cal-x > eat[-1][0]:
            now = x
            eat.append((cal-x,now))
        else:
            eat.append((eat[-1][0],now))
        cx,cv = j
        ccal += cv
        if ccal-(C-cx) > ceat[-1][0]:
            cnow = C-cx
            ceat.append((ccal-(C-cx),cnow))
        else:
            ceat.append((ceat[-1][0],cnow))
    
    ceat.reverse()
    ans = 0
    for i,j in zip(eat,ceat):
        eat,x = i
        ceat,cx = j
        ans = max(ans,eat+ceat-min(x,cx))

    print(ans)

if __name__ == "__main__":
    main()