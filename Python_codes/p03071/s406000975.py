a,b = map(int, input().split())
num = 0
for i in range(2):
    if a <= b:
        num += b
        b -= 1
    else:
        num += a
        a -= 1
print(num)