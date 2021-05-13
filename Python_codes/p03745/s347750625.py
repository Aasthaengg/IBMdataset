num = int(input())
l = list(map(int, input().split()))
count = 1
var = var2 = 0
c = l[0]
for i in l[1:]:
    if c < i:
        var = 1
    elif c > i:
        var2 = 1
    if var == 1 and var2 == 1:
        count += 1
        var = var2 = 0
    c = i
print(count)