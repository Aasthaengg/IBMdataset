import collections
import sys

def read_prob():
    inputs = []
    try:
        counter = 0
        while True:
            if counter == 0:
                line = input().strip()
                size = int(line)
            else:
                line = input().strip().split()
                a, b, c = line[0], line[1], line[2]
                inputs.append([int(a),  int(b), int(c)])
            counter += 1
    except EOFError:
        pass
    return inputs

def triangle(inputs):
    f = lambda x: x * x
    inputs = list(map(f, inputs))
    # print(inputs)
    a, b, c = inputs[0], inputs[1], inputs[2]
    if a + b == c:
        return True
    elif a + c == b:
        return True
    elif b + c == a:
        return True
    else:
        return False

if __name__ == '__main__':
    inputs = read_prob()
    for inp in inputs:
        if triangle(inp):
            print("YES")
        else:
            print("NO")

