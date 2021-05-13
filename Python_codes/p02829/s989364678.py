A=input()
B=input()

List=["1","2","3"]

del List[List.index(A)]
del List[List.index(B)]

print("".join(List))
