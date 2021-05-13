n,m,x,y = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = "War"
am = max(a)
bm = min(b)
for z in range(x+1,y+1):
    if am<z and bm>=z:
        ans = "No War"
        break
print(ans)