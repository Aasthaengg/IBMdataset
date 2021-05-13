import sys
a, b, c = map(int, input().split())
var = 0
for i in range(1000):
    if a%2 != 0 or b%2 != 0 or c%2 != 0:
        print(var)
        sys.exit()
    a, b, c = b/2 + c/2, a/2 + c/2, a/2 + b/2
    var += 1
print(-1)