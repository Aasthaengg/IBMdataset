num_list = [int(input()) for _ in range(3)]
X = num_list[0]
A = num_list[1]
B = num_list[2]
X -= A
while X >= B:
    X -= B
print(X)