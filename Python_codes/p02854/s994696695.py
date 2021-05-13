n = int(input())
a = list(map(int,input().split()))
SUM = sum(a)
cnt = 0
l = []
for i in range(n):
    cnt += a[i]
    l.append(abs(cnt - (SUM - cnt)))
print(min(l))