n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if sum(a) < sum(b):
    print(-1)
else:
    d = [a[i] - b[i] for i in range(n)]
    count = 0
    num = 0
    for i in d:
        if i < 0:
            count += 1
            num += i
    d.sort(reverse = True)
    for i in d:
        if num >= 0:
            break
        num += i
        count += 1
    print(count)
