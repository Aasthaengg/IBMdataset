n = int(input())
a = list(map(int, input().split()))
ab = [abs(i) for i in a]
cnt = 0
for i in a:
    if i < 0:
        cnt += 1
if 0 in a or cnt % 2 == 0:
    print(sum(ab))
else:
    print(sum(ab) - min(ab) * 2)