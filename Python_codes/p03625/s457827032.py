from collections import Counter
n = int(input())
a = Counter(map(int, input().split()))
x = [0, 0]
for i in a.keys():
    if a[i] >= 2:
        x.append(i)
    if a[i] >= 4:
        x.append(i)
x.sort(reverse=True)
print(x[0] * x[1])