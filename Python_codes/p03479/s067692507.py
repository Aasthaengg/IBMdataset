x,y=map(int,input().split())
s=x
cnt=0
while True:
    s*=2
    cnt+=1
    if s>y:
        break
print(cnt)