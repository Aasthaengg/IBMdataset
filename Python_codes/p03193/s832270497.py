N,H,W = map(int,input().split())

res = 0

for i in range(N):
    a,b = map(int,input().split())
    if H <= a and W <= b:
        res += 1
print(res)