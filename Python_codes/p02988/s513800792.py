n = int(input())
p = list(map(int, input().split()))
counter = 0
for i in range(1, n - 1):
    temp = [p[i - 1], p[i], p[i + 1]]
    temp.sort()
    if temp[1] == p[i]:
        counter += 1
print(counter)
