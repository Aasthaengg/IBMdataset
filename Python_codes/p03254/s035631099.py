n, x = map(int, input().split())
a = list(map(int, input().split()))
sum_a = sum(a)
cnt = 0
a.sort()
if x > sum_a:
    cnt = n - 1
elif x == sum_a:
    cnt = n
else:
    for i in a:
        if i <= x:
            x -= i
            cnt += 1
        else:
            break
print(cnt)