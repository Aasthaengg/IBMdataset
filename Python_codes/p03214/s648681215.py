n = int(input())
a = list(map(int,input().split()))

mean = sum(a)/n
now = 0
sa = 10**10

for i,j in enumerate(a):
    if abs(mean-j) < sa:
        now = i
        sa = abs(mean-j)

print(now)