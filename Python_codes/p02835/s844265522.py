A=[int(s) for s in input().split()]

print("bust" if sum(A)>=22 else "win")