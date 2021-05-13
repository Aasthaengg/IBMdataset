k, t = map(int, input().split())
a = [int(_) for _ in input().split()]

if t == 1:
    print(k-1)
else:
    a.sort(reverse=True)
    num = a[0] - 1
    cnt = 0
    for i in range(1, t):
        cnt += a[i]
    print(max(num-cnt, 0))