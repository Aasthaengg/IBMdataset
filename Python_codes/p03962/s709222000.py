a,b,c=map(int,input().split())
cnt=3

if a==b:
    cnt-=1

if b==c:
    cnt-=1

if c==a:
    cnt-=1

if a==b==c:
    cnt+=1

print(cnt)