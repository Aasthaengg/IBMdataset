import sys

def main():
    h, w, m = map(int,input().split())
    bomb = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(m)]
    x = [0] * h
    y = [0] * w

    for h,w in bomb:
        x[h] +=1
        y[w] +=1

    maxX = max(x)
    maxY = max(y)

    r = [h for h,x in enumerate(x) if x == maxX]
    c = [w for w,y in enumerate(y) if y == maxY]

    bomb = set(bomb)
    
    for ri in r:
        for ci in c:
            if (ri,ci) not in bomb:
                print(maxX + maxY)
                sys.exit()
    print(maxX + maxY -1)
    
main()
