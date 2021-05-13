n = int(input())
a = list(map(int, input().split()))

forward = True
sec, first = [], []
for i in range(n):
    if i%2:
        first.append(a[i])
    else:
        sec.append(a[i])
arr = first[::-1] + sec
if len(first) != len(sec):
    arr = arr[::-1]

for el in arr:
    print(el, end=' ')