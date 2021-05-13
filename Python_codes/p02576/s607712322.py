x,n,t = map(int,input().split(" "))
cnt =0
while x > 0:
    x -= n
    cnt += 1
print(cnt * t)