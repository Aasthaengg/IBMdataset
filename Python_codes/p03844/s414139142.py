# ABC 050: A – Addition and Subtraction Easy
parts = [s for s in input().split()]
print(int(parts[0]) + int(parts[2]) if parts[1] == '+' else int(parts[0]) - int(parts[2]))