_ = int(input())
a = sorted(list(map(int, input().split())))
num0, num1, val = a[-1], 0, float('inf')

for i in a[:-1]:
    val0 = abs(i-num0/2)
    if val0 < val:
        num1 = i
        val = val0
print(num0, num1)
