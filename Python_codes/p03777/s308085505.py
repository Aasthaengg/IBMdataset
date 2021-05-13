a, b = [s == "H" for s in input().split()]
f = b if a else not b
print("H" if f else "D")