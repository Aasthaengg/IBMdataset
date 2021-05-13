h,w,a,b = list(map(int,input().split()))

ans = [['0']*w for i in range(h)]
for y in range(h):
    for x in range(w):
        if x<a and y<b:
            ans[y][x]="1"
        elif x>=a and y>=b:
            ans[y][x]="1"

for a in ans:
    print("".join(a))