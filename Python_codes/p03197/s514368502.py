n = int(input())
for _ in range(n):
    if int(input()) % 2 == 1:
        print("first")
        break
else:
    print("second")