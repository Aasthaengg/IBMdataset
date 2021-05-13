n, m, x, y = map(int, input().split())
xmax = max(list(map(int,input().split())))
ymin = min(list(map(int,input().split())))
        
if min(ymin, y) - max(xmax, x) >= 1:
    print("No War")
else:
    print("War")
