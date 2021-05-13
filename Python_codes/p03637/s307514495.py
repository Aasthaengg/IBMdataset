N = int(input())
A = map(int, input().split())
var0 = 0
var1 = 0
var2 = 0

for a in A:
    if a % 4 == 0:
        var2 += 1
    elif a % 2 == 0:
        var1 += 1
    else:
        var0 += 1

var1 %= 2
ans = 'Yes' if var2 >= var1 + var0 - 1 else 'No'
print(ans)
