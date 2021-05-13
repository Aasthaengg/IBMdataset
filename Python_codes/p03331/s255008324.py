line = input()
num = [int(n) for n in line.split()][0]
number_of_sums = num//2 + 1 + 1*num % 2
smallest_sum = 100000
for i in range(1, number_of_sums):
    first_number = i
    second_number = num-i
    summation = 0
    while first_number and summation < smallest_sum:
        summation += first_number % 10
        first_number //= 10
    while second_number and summation < smallest_sum:
        summation += second_number % 10
        second_number //= 10
    if smallest_sum > summation:
        smallest_sum = summation
print(smallest_sum)