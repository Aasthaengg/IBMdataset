import sys
n = int(input())
cake = 4
donut = 7
for i in range(25):
    for j in range(15):
        if cake*i+donut*j == n:
            print("Yes")
            sys.exit()
print("No")