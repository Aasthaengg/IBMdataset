input_line = input()
inputs = input_line.split(' ')
inputs = [int(input) for input in inputs]

A = inputs[0]
B = inputs[1]

dual_B = 2 * B

res = 0
if A > dual_B:
    res = A - dual_B
else:
    res = 0

print(res)
