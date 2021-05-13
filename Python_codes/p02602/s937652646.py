n, k = map(int, input().split())
a = list(map(int, input().split()))
target = a[0:k]
for i in a[k:n]:
    if i > target.pop(0):
        print('Yes')
    else:
        print('No')
    target.append(i)