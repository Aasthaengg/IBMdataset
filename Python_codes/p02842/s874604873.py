N = int(input())

for i in range(50000):
    if N == i*108//100:
        print(i)
        break
else:
    print(":(")