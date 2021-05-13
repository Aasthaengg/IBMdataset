N = int(input())

if N > 81 or N == 0:
    print("No")
    exit()

for i in range(1, 10):
    for j in range(1, 10):
        if i * j == N:
            print("Yes")
            exit()
print("No")
