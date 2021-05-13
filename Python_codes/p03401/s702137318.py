n = int(input())
a = list(map(int, input().split()))
a.append(0)

lst = []
before = 0
for num in a:
    lst.append(abs(num - before))
    before = num
total = sum(lst)
for i in range(n):
    if i == 0:
        print(total - lst[i] - lst[i + 1] + abs(a[i+1]))
    else:
        print(total - lst[i] - lst[i + 1] + abs(a[i - 1] - a[i + 1]))