A = int(input())
B = int(input())

cands = list(range(1,4))
cands.remove(A)
cands.remove(B)
print(cands[0])