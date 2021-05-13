n = int(input())
values = list(map(int, input().split()))

if n == 2:
    ans = (values[0] + values[1])/2
else:
    while len(values) > 1:
        values.sort()
        tmp = (values[0] + values[1])/2
        values.pop(0)
        values.pop(0)
        values.append(tmp)
    ans = values[0]

print(ans)