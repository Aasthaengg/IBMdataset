n = int(input())
a = list(map(int, input().split()))
data = []
for i in range(n):
    for j in range(len(a)):
        if a[len(a) - j - 1] == len(a) - j:
            data.append(a[len(a) - j - 1])
            del a[len(a) - j - 1]
            break
if len(data) == n:
    data.reverse()
    for x in data:
        print(x)
else:
    print(-1)