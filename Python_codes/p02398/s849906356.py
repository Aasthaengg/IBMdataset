count = 0
string = input()
numbers = string.split(' ')
x, y, z = int(numbers[0]), int(numbers[1]), int(numbers[2])
while x <= y:
    if z%x == 0:
        count += 1
    x += 1
print(count)
        
