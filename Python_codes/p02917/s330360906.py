n = int(input())
a = [1e10]
b = list(map(int, input().split()))
for i, num in enumerate(b):
    if a[i] > num:
        a[i] = num
    a.append(num)
print(sum(a))