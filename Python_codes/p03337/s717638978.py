line = input()
num_a, num_b = [int(n) for n in line.split()]
print(max([num_a + num_b, num_a - num_b, num_a * num_b]))