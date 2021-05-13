#068_D
k = int(input())
x = -(-k // 50)
y = x * 50 - k
a = [i+(x-1) for i in range(1, 51)]
for _ in range(y):
    a.sort()
    for i in range(50):
        a[i] += 1
    a[-1] -= 51
a.sort()
print(50)
print(*a)