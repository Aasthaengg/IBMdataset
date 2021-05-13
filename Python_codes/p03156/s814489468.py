n = int(input())
a, b = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
cnt = [0,0,0]
for i in range(n):
    if p[i] <= a:
        cnt[0] += 1
    elif p[i] >= b+1:
        cnt[2] += 1
    else:
        cnt[1] += 1

print(min(cnt))