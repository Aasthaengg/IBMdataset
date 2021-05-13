a,b = map(int,input().split())
INF = 200005

big = max(a,b)
small = min(a,b)

for x in range(big,big*small+1,big):
    if x % small == 0:
        print(x)
        break
