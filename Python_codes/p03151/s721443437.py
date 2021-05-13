n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
if sum(a) < sum(b):
    ans = -1
else:
    c = [b[i] - a[i] for i in range(n)]
    c.sort()
    c_minus = [cc for cc in c if cc > 0]
    if len(c_minus) == 0:
        ans = 0
    else:
        aaa = 0
        point = sum(c_minus)
        for i in range(n):
            point += c[i]
            if point <= 0:
                break
        ans = len(c_minus) + i + 1
print(ans)