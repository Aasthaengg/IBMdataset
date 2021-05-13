N = int(input())
A = list(int(input())for i in range(N))
for i in A:
    if i % 2 == 1:
        print("first")
        exit()
print("second")