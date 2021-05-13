n = int(input())
alst = [int(input()) for _ in range(n)]
for num in alst:
    if num % 2 == 1:
        print("first")
        break
else:
    print("second")