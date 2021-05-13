n=int(input())
ab=[list(map(int, input().split())) for _ in range(n)]

cnt=0
for i in range(n):
    a=ab[n-i-1][0]
    b=ab[n-i-1][1]
    a+=cnt
    amari=a%b
    shou=a//b
    if amari!=0:
        cnt+=b-amari
print(cnt)