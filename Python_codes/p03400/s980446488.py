n = int(input())
d,x = list(map(int,input().split()))
cnt = 0
for i in range(n):
    a = int(input())
    stay = 1
    while d>=stay:
        stay+=a
        cnt += 1

print(cnt+x)