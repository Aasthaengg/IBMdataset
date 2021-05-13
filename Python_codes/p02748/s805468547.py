a,b,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
lists = [list(map(int,input().split())) for i in range(m)]
Min = min(a) + min(b)
for x,y,c in lists:
    Min = min(Min,a[x-1] + b[y-1] - c)
print(Min)

