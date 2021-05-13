a,b = input().split()
a = 1 if a == "H" else -1
b = 1 if b == "H" else -1

print("H" if a*b == 1 else "D")
