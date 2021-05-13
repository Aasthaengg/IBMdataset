N = input()
A = N[0] == N[1] == N[2]
B = N[1] == N[2] == N[3]

print("Yes" if A or B else "No")