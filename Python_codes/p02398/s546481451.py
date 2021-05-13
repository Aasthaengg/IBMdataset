numbers = input().split()
numbers = list(map(int, numbers))

answer = 0

for i in range(numbers[0],numbers[1]+1):
    if numbers[2]%i == 0:
        answer+=1

print(answer)