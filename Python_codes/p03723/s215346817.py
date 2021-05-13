a,b,c=map(int, input().split())

cnt=0
for _ in range(10**5):
    if a%2==1 or b%2==1 or c%2==1:
        print(cnt)
        exit()
    a,b,c=b//2+c//2,c//2+a//2,a//2+b//2
    cnt+=1
print(-1)
