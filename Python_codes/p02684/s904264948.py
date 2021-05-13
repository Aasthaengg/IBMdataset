#167_d
n, k = map(int, input().split())
a = list(map(int, input().split()))

r = []
check = [0]*len(a)
now = 1
count = 0

while True:
    r.append(now)
    now = a[now - 1]
    
    if check[now - 1] == 1:
        roop = r[r.index(now):]
        break
    check[now - 1] += 1
    
if len(r) - 1 >= k: #ループに入らないとき
    print(r[k])
else:#ループに入ったとき
    print(roop[(k-len(r)) % len(roop)])