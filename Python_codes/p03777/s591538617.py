dic = {("H", "H"): "H", ("H", "D"): "D", ("D", "D"): "H", ("D", "H"): "D"}
a, b = input().split()
print(dic[(a, b)])