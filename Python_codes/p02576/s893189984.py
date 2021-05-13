n,x,t = map(int,input().split())

cnt = 0
while n > 0:
    n = n - x
    cnt += 1

print(cnt*t)
