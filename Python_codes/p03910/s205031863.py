n = int(input())
val, a = 0, 1

while val <= n:
    val += a
    a += 1
b = val-n
for i in range(1, a):
    if i != b:
        print(i)
