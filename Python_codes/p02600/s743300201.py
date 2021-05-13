x = int(input())
sum = 600
for i in range(8, 0, -1):
    if x < sum:
        print(i)
        break
    sum += 200