# AGC 004: A – Divide a Cuboid
n = [int(s) for s in input().split()]
n.sort()

print(n[0] * n[1] if n[2] % 2 == 1 else 0)