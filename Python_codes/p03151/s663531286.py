n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if sum(a)<sum(b):
    result = -1
else:
    count = 0
    over = [0]
    result = 0
    for i in range(n):
        if a[i]>b[i]:
            over.append(a[i]-b[i])
        elif a[i]<b[i]:
            count += b[i]-a[i]
            result += 1
    over.sort(reverse=True)
    i = 0
    while count > 0:
        result += 1
        count -= over[i]
        i += 1
print(result)