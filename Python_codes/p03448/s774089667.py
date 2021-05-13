abc = [int(input()) for i in range(3)]
x = int(input())

count = 0

for i in range(abc[0] + 1):
    for j in range(abc[1] +1):
        for k in range(abc[2] +1):
            if 500*i + 100*j + 50*k == x:
                count += 1
print(count)