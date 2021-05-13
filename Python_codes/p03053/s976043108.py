from collections import deque
def main():
    h,w = map(int,input().split())
    S = [list(input()) for i in range(h)]
    q = [(i,j) for i,a in enumerate(S) for j,b in enumerate(a) if b=='#']
    q = deque(q)
    ans = 0
    s = h*w
    cnt = len(q)
    nxt = [(0,1),(1,0),(-1,0),(0,-1)]
    while cnt < s:
        ans += 1
        q_ = deque([])
        while q:
            a,b = q.pop()
            for x,y in nxt:
                X,Y = a+x,b+y
                if 0>X or X>h-1 or 0>Y or Y>w-1:
                    continue
                if S[X][Y]=='.':
                    S[X][Y]='#'
                    q_.append((X,Y))
        q = q_
        cnt += len(q_)
    print(ans)

if __name__ == "__main__":
    main()