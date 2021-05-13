n = input()
m = n.translate(str.maketrans({"1": "9", "9": "1"}))
print(m)