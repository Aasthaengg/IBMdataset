A, B = input().split()
AB = int(str(A) + str(B))
print("Yes" if AB % (AB ** 0.5) == 0 else "No")
