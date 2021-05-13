def solve():
    n = int(input())
    
    P = set()
    for i in range(n):
        x,y,h = map(int,input().split())
        if h != 0:
            P.add((x,y,h))
    x,y,h = P.pop()
    if not P:
        return x,y,h
    for cx in range(101):
        for cy in range(101):
            H = h + abs(x-cx) + abs(y-cy)
            for p in P:
                if H != p[2] + abs(p[0]-cx) + abs(p[1]-cy):
                    break
            else:
                return cx,cy,H
        
if __name__ == '__main__':
    print(*(solve()))
