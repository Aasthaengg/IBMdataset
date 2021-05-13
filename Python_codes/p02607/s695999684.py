n = int(input())

mas = list(map(int, input().split(' ')))

count = 0

for i in range(len(mas)):
    if((i + 1) % 2 == 1):
        if(mas[i] % 2 == 1):
            count += 1

print(count)