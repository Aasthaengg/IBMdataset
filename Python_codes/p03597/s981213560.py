n_line = int(input())
num_a_painted_white = int(input())

total_space = n_line * n_line
num_a_painted_black = total_space - num_a_painted_white

print(num_a_painted_black)