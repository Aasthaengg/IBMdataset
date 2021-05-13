k, x = map(int, input().split())
a = ''
for i in range(x - k + 1, k + x - 1):
    a += str(i) + ' '
a += str(k + x - 1)
print(a)