h,w = map(int,input().split())
n = int(input())
al = list(map(int,input().split()))

ansl = [[0 for _ in range(w)] for _ in range(h)]

idx = 0
for color, a in enumerate(al):
    for i in range(a):
        yoko = idx % w
        tate = idx // w
        if tate % 2 == 1:
            yoko = w - yoko - 1 
        ansl[tate][yoko] = str(color+1)
        idx += 1

for ans in ansl:
    print(" ".join(ans))