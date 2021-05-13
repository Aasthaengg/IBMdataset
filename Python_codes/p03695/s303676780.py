n = int(input())
a = list(map(int, input().split()))
cnt = []
over = 0
for i in range(n):
    m = a[i] // 400
    if m < 8:
        if m not in cnt:
            cnt.append(m)
    else:
        over += 1
if len(cnt) > 0:
    print(len(cnt), len(cnt)+over)
else:
    print(1, len(cnt)+over)
