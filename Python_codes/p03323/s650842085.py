line = input()
num_a, num_b = [int(n) for n in line.split()]
is_it_possible = "Yay!"
if num_a > 8 or num_b > 8:
    is_it_possible = ":("
print(is_it_possible)