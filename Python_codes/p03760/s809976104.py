O = input()
E = input()

l = [0]*(len(O)+len(E))

l[0::2] = list(O)

l[1::2] = list(E)

print("".join(l))