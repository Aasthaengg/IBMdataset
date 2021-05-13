from collections import defaultdict
H,W = map(int,input().split())
d = defaultdict(int)
for _ in range(H):
    for c in list(input()):
        d[c] += 1
for i in range((H-1)//2+1):
    for j in range((W-1)//2+1):
        s = set([(x,y) for x,y in [(i,j),(i,W-1-j),(H-1-i,j),(H-1-i,W-1-j)] if 0<=x<H and 0<=y<W])
        f = True
        for k,_ in sorted(d.items(),key=lambda x:x[1]):
            if d[k] >= len(s):
                d[k] -= len(s)
                f = False
                break
        if f:
            print("No")
            exit(0)
print("Yes")