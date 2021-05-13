N = int(input())

Alist = list(map(int, input().split()))
plus = [abs(a) for a in Alist]

cnt = 0

for a in Alist:
    if a < 0:
        cnt += 1

if cnt%2==0:
    print(sum(plus))
else:
    print(sum(plus) - min(plus) * 2)