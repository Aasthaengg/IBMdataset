W = input()
a = []
while True:
    T = input()
    if T == "END_OF_TEXT":
        break
    a += [j.lower() for j in T.split()]
print(a.count(W))