numbers = input()
numbers = numbers.split(" ")
ball_number = int(numbers[0])
person_number = int(numbers[1])

result = 0

if person_number > 1:
  result = ball_number - person_number
  
print(result)
