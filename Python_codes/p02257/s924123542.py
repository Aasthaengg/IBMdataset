import math

def isPrime(num):
    for i in range(int(math.sqrt(num)), 1, -1):
        if num % i == 0:
            return None
    return num

inputs = []

while True:
    try:
        inputs.append(input())
    except(EOFError):
        break

inputs.pop(0)

print(len([x for x in list(map(isPrime, map(int, inputs))) if x is not None]))

