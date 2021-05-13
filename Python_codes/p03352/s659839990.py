x = int(input())
if x == 1:
    print(1)
    exit()

for i in reversed(range(1, x + 1)):
    for j in range(2, 101):
        for k in range(2, 101):
            number = j ** k
            if number == i:
                print(i)
                exit()
