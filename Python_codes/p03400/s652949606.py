n=int(input())
d,x=map(int,input().split())

ans=0

for i in range(n):
    cnt = 1
    a =int(input())
    j=1
    while a*j+1<= d:
        cnt += 1
        j += 1
    ans += cnt
total = x + ans
print(total)