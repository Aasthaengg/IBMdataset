N = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
val = 0
pre = -1
for i in a:
    if pre == i-1:
        val += c[pre-1]
    val += b[i-1]
    pre = i
print(val)
