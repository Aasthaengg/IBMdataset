n = int(input())
d, x = map(int, input().split())
cnt = 0
a = [int(input()) for i in range(n)]

for i in range(len(a)):
    t = d // a[i]
    for j in range(t+1):
        if d >= j*a[i]+1:
            cnt += 1
            
print(cnt+x)