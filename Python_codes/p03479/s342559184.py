X, Y = [int(i) for i in input().split()]

output = 0

while Y >= X:
    X = 2 * X
    output += 1
    
print(output)