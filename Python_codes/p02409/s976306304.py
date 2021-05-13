b1 = [[0 for i in range(10)] for j in range(3)]
b2 = [[0 for i in range(10)] for j in range(3)]
b3 = [[0 for i in range(10)] for j in range(3)]
b4 = [[0 for i in range(10)] for j in range(3)]

n = int(input())
i = 1
while i <= n:
    b, f, r, v = map(int, input().split())
    if (b == 1):
        b1[f-1][r-1] += v
    elif (b == 2):
        b2[f-1][r-1] += v
    elif (b == 3):
        b3[f-1][r-1] += v
    elif (b == 4):
        b4[f-1][r-1] += v
    i += 1

for i in range(3):
    print('', ' '.join(map(str, b1[i])))
print('#' * 20)
for i in range(3):
    print('', ' '.join(map(str, b2[i])))
print('#' * 20)
for i in range(3):
    print('', ' '.join(map(str, b3[i])))
print('#' * 20)
for i in range(3):
    print('', ' '.join(map(str, b4[i])))