#   Transfer

a, b, c = map(int, input().split())

residue = c - (a - b)
if residue<0:
    residue=0

print(residue)

