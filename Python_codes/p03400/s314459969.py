n = int(input())
d,x = map(int,input().split())
a = [int(input()) for _ in range(n)]

cnt = [1]*n
for i in range(n):
    num = (d-1)//a[i]
    cnt[i] += num

print(x + sum(cnt))