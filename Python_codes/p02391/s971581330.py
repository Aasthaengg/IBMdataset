a, b = [int(i) for i in input().split()]
s = "=="
if a < b: s = "<"
elif a > b: s = ">"
print("a", s, "b")