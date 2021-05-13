n = int(input())
a = [int(input()) for _ in range(n)]
top1, top2 = sorted(a, reverse=True)[:2]
for num in a:
    if num==top1:
        print(top2)
    else:
        print(top1)
