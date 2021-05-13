n = int(input())
ab=[list(map(int,input().split())) for i in range(n)]
cnt=0
for i in reversed(range(n)):
    a,b=ab[i]
    a+=cnt
    if a%b==0:
        continue
    if a<=b:
        cnt+=(b-a)
        continue
    cnt += -(-a//b) * b - a
print(cnt)