string = input()
index_of_A = string.index("A")
index_of_Z = string.rfind("Z")

print(index_of_Z - index_of_A + 1)
