a,b,m = map(int, input().split())

ai = list(map(int, input().split()))
bi = list(map(int, input().split()))
tmp_min = min(ai) + min(bi)

for i in range(m):
    x,y,c = map(int, input().split())
    z = ai[x-1] + bi[y-1] - c
    if z < tmp_min:
        tmp_min =  z

print(tmp_min)