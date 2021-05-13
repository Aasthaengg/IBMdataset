W,H,N = map(int,input().split())
height = set([])
wigth = set([])
for i in range(N):
    x,y,a = map(int,input().split())
    if a == 1:
        for i in range(x):
            wigth.add(i)
    elif a == 2:
        for i in range(x,W):
            wigth.add(i)
    elif a == 3:
        for i in range(y):
            height.add(i)
    else:
        for i in range(y,H):
            height.add(i)
print((H-len(height))*(W-len(wigth)))