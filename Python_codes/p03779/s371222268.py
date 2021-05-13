x=int(input())
for i in range(x):
    if i * (i + 1) // 2>= x:
        print(i)
        exit()
print(x)