import math

while True:
    number_of_input = int(raw_input())
    if number_of_input == 0:
        break
    values = [float(x) for x in raw_input().split()]
    second_moment = sum([x ** 2.0 for x in values]) / number_of_input
    first_moment = sum([x for x in values]) / number_of_input
    print math.sqrt(second_moment - first_moment ** 2.0)