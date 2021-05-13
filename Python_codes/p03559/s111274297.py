import bisect

n = int(input())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))
c = sorted(list(map(int,input().split())))

ue = []
for i in range(n):
    ue.append(bisect.bisect_left(a,b[i]))

sita = []
for i in range(n):
    sita.append(n - bisect.bisect_right(c,b[i]))

ans = 0
for i in range(n):
    ans += ue[i]*sita[i]

print(ans)
