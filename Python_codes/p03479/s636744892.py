x,y=map(int,input().strip().split())

cnt=1
while True:
    x*=2
    if x<=y:
        cnt+=1
    else:
        break

print(cnt)