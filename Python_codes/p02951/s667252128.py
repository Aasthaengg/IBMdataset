#   Transfer

def return_residue(a, b, c):
    residue = c - (a - b)
    return max(0, residue)


a, b, c = map(int, input().split())

print(return_residue(a, b, c))
